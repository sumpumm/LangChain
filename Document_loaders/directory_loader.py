from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='F:\\SAMARPAN\\LangChain\\Document_loaders\\books',
    glob='*.pdf', #this is the pattern to specify which type of file. in this case it means extract all pdf files. see patterns in docs.
    loader_cls=PyPDFLoader #specify which loader class you are going to use
)

# docs = loader.load()

# print(len(docs))

docs = loader.lazy_load()
for doc in docs:
    print(doc.metadata)