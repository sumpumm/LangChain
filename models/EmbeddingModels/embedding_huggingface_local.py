from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

text = "My name is samarpan"

#embedding a single sentence
vector = embedding.embed_query(text)

print(vector)

#embediing documents
documents=[
    "My name is samarpan",
    "i am 22 years old",
    "i live in jhamsikhel"
]

vector2= embedding.embed_documents(documents) #it give 2d list

print(str(vector2))