from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt = PromptTemplate(
    template="answer the following question \n {question} from the following text: \n{text}",
    input_variables=['question', 'text'],
    validate_template= True
)

#Web  base loader is mainly used for static webpages and are htmml heavy.
url = 'https://www.daraz.com.np/products/light-bulb-camera-light-socket-security-camera-two-way-audio-capability-for-home-i132007395-s1039807501.html?pvid=5ebfbd23-c31c-4b8d-8fd5-06aa393c91e3&search=jfy&scm=1007.51705.413671.0&spm=a2a0e.tm80335409.just4u.d_132007395'
loader =  WebBaseLoader( web_path=url)

docs = loader.load()

# print(len(docs))

# print(docs)

chain = prompt | model | parser

result = chain.invoke({
    'question': 'what is the product and tell me its price',
    'text': docs[0].page_content
})

print(result)