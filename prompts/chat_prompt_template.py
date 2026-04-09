from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human',"Explain in simpple terms, what is {topic}")
])

model = ChatHuggingFace(llm=llm)

chain = chat_template | model

result = chain.invoke({
    'domain':'machine learning',
    'topic':'linear regression'
})

print(result.content)