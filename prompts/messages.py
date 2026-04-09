from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm) 

chat = [
    SystemMessage(content='You are a helpful AI assistant'),
    HumanMessage(content='Tell me a joke'),
]

result = model.invoke(chat)
chat.append(AIMessage(content=result.content))

print(chat)