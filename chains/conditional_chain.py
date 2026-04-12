from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_classic.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1= PromptTemplate(
    template='Classify the following feedback as positive or negative: \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'text':'this is a terrible smartphone'}).sentiment

prompt2 = PromptTemplate(
    template='Write an appropriate response for this positifve feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response for this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive',  prompt2 | model | parser1),
    (lambda x:x.sentiment=='negative',  prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment") # default chain
)

final_chain = classifier_chain | branch_chain

result = final_chain.invoke({'feedback':'this is a terrible smartphone'})

print(result)