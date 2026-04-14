from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Building Machine Learning Systems with Python - Second Edition.pdf')

docs = loader.load()

# print(docs[0].page_content)
# print(docs[0].metadata)

print(docs[2])