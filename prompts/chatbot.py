from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)
chat_history =[]

model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("You : ")
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI : ", result.content)

print(chat_history)