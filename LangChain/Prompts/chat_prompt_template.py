
# ChatPromptTemplate is a template for creating chat-based prompts. It allows you to define a sequence of messages with different roles (e.g., system, human, assistant) and then fill in the placeholders with specific values when invoking the template.

# These are also called dynamic prompts, as they can be customized with different inputs at runtime.

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)

# '''
'''
(langchain-prompts-main) PS C:\Users\samin\Python\Campusx\langchain-models-master\langchain-prompts-main_2\langchain-prompts-main> uv run .\chat_prompt_template.py
messages=[SystemMessage(content='You are a helpful cricket expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms, what is Dusra', additional_kwargs={}, response_metadata={})]
'''