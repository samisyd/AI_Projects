# MessagesPlaceholder is a special type of placeholder used in chat prompt templates to represent a list of messages that can be dynamically filled in when invoking the template. It allows you to include a variable number of messages in the chat history, which can be useful for maintaining context in a conversation.

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)