# %%
# Load documents from web
from langchain.document_loaders import WebBaseLoader

web_loader = WebBaseLoader([
    "https://python.langchain.com/docs/get_started/introduction",
    "https://python.langchain.com/docs/modules/data_connection/"
])

data = web_loader.load()


# %%
# Split documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 0
)

all_splits = text_splitter.split_documents(data)

all_splits[0]
# output: 


# %%
# Transform into Text Embeddings and Store at Chroma Vector DB
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

os.environ["OPENAI_API_KEY"] = "sk-xxxxxx...."

vectorstore = Chroma.from_documents(
    documents=all_splits,
    embedding=OpenAIEmbeddings()
)


# %%
# RAG prompt
from langchain import hub 

prompt = hub.pull("rlm/rag-prompt")

print(prompt)
# output: 


# %%
# LLM Model
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

model = ChatOpenAI(model_name="gpt-4", temperature=0)


# %%
# Retrieval QA
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    retrievar=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": prompt}
)

question = "What is a LangChain?"
result = qa_chain({"query": question})

result["result"]
# output: 


# %%
question = "What is Retrieval in LangChain?"
result = qa_chain({"query": question})

result["result"]
# output: 


# %%