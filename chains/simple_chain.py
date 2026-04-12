from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

template = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

chain = template | model | parser

result = chain.invoke({'topic':'Linear regression'})
print(result)