from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), # what this does is that it makes a place in the prompt to insert previous chat history
    ('human','{query}')
])

#load the chat history
chat_history=[]
with open('prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

model = ChatHuggingFace(llm=llm)

chain = chat_template | model

result = chain.invoke({
    'chat_history' : chat_history,
    'query' : 'where is my refund?'
})

print(result.content)