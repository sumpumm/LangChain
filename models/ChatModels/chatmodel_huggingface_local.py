from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

# Create the HuggingFace pipeline manually
pipe = pipeline(
    task="text-generation",            # LLaMA chat models use text-generation
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1,                         # CPU (-1), GPU >=0 if compatible
    temperature=0.5,
    max_new_tokens=100
)

# Wrap the pipeline in LangChain
llm = HuggingFacePipeline(pipeline=pipe)

# Create chat interface
model = ChatHuggingFace(llm=llm)

# Invoke model
result = model.invoke("Who is Balendra Shah?")

# Print output
print(result.content) 