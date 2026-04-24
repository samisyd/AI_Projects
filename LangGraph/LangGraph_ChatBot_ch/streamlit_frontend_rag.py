from chatbot_rag_backend import ( 
    chatbot, 
    chatbot_with_memory, 
    get_all_threads,
    ingest_pdf,    
    thread_document_metadata
)
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import streamlit as st
import uuid

# ********************* Utility Functions ************************
def generate_thread_id():
    return str(uuid.uuid4())

def reset_chat():
    st.session_state["message_history"] = []    
    st.session_state["name"] = ""
    st.session_state['thread_id'] = ""

def add_thread(thread_id, name=""):
    if "chat_threads" in st.session_state:
        # Avoid duplicate thread IDs in the list
        if not any(t[0] == thread_id for t in st.session_state['chat_threads']):
            st.session_state['chat_threads'].append([thread_id, name])

def load_conversation(thread_id):
    state = chatbot_with_memory.get_state(config={"configurable": {"thread_id": thread_id}})
    messages = state.values.get('messages', [])
    return messages

# ********************* Session setup ************************
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = ""

if "name" not in st.session_state:
    st.session_state["name"] = ""

if "chat_threads" not in st.session_state:    
    st.session_state["chat_threads"] = get_all_threads()

if "ingested_docs" not in st.session_state:
    st.session_state["ingested_docs"] = {}

# Current thread context
thread_key = st.session_state["thread_id"]
thread_docs = st.session_state["ingested_docs"].get(thread_key, {})

# ********************* SideBar UI ************************
st.sidebar.title("Langgraph PDF Chatbot")

if st.sidebar.button("New chat"):
    reset_chat()
    st.rerun()

# PDF Display logic
if thread_docs:
    latest_doc = list(thread_docs.values())[-1]
    st.sidebar.success(f"Using `{latest_doc.get('filename')}`")
else:
    st.sidebar.info("No PDF indexed for this thread.")

uploaded_pdf = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_pdf and thread_key:
    if uploaded_pdf.name in thread_docs:
        st.sidebar.info(f"`{uploaded_pdf.name}` already processed.")
    else:
        with st.sidebar.status("Indexing PDF…") as status_box:
            summary = ingest_pdf(
                uploaded_pdf.getvalue(),
                thread_id=thread_key,
                filename=uploaded_pdf.name,
            )
            st.session_state["ingested_docs"].setdefault(thread_key, {})[uploaded_pdf.name] = summary
            status_box.update(label="✅ PDF indexed", state="complete")

st.sidebar.header("My Conversations")
# Reverse to show newest at top
threads = st.session_state["chat_threads"][::-1]

for t_id, t_name in threads:
    # FIX: Using a unique key for each button and avoiding name collisions
    if st.sidebar.button(label=t_name or t_id[:8], key=f"btn_{t_id}"):
        st.session_state["thread_id"] = t_id
        st.session_state["name"] = t_name
        
        # Load history
        raw_msgs = load_conversation(t_id)
        formatted_msgs = []
        for m in raw_msgs:
            role = "user" if isinstance(m, HumanMessage) else "assistant"
            # Only add messages that have content
            if m.content:
                formatted_msgs.append({"role": role, "content": m.content})
        
        st.session_state["message_history"] = formatted_msgs
        st.rerun()

# ********************* Main Chat UI ************************
st.title("Chatbot with Langgraph")

# Render history
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    # Initialize thread if empty
    if st.session_state["thread_id"] == "":
        st.session_state["thread_id"] = generate_thread_id()
    
    current_tid = st.session_state["thread_id"]
    
    # Display user message
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate Name if it's a new conversation
    if st.session_state["name"] == "":
        chatbot_response = chatbot.invoke({"messages": [HumanMessage(content=f"Create a 3 word title for: {user_input}")]})
        generated_name = chatbot_response["messages"][-1].content
        st.session_state["name"] = generated_name
        add_thread(current_tid, generated_name)

    CONFIG = { 
        "configurable": {"thread_id": current_tid}, 
        "metadata": {"thread_id": current_tid},
    }

    # Assistant streaming block
    with st.chat_message("assistant"):
        status_holder = {"box": None}

        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            ):
                if isinstance(message_chunk, ToolMessage):
                    if status_holder["box"] is None:
                        status_holder["box"] = st.status("🔧 Searching documents...", expanded=True)
                
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content
    
        ai_message = st.write_stream(ai_only_stream())

        if status_holder["box"] is not None:
            status_holder["box"].update(label="✅ Search complete", state="complete", expanded=False)
    
        st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
    
    st.rerun()