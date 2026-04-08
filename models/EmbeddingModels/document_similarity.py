from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding_model = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Artificial Intelligence is transforming industries by enabling machines to learn from data and make decisions.",
    
    "Kathmandu is the capital city of Nepal, known for its rich culture, temples, and historical heritage sites.",
    
    "Football is one of the most popular sports in the world, played by millions of people across different countries.",
    
    "Healthy eating includes consuming a balanced diet with fruits, vegetables, proteins, and whole grains.",
    
    "Python is a versatile programming language widely used for web development, data science, and machine learning."
]   

query = "Tell me about the capital of Nepal"

doc_embeddings = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)

similarity_scores = cosine_similarity([query_embedding],doc_embeddings)[0] #embeddings must be passed in 2D list
index, score = sorted(list(enumerate(similarity_scores)), key= lambda x:x[1])[-1]

print(documents[index])
print("Similarity Score is ", score)
