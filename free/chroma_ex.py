# %%
# Create a Chroma Client
import chromadb

chroma_client = chromadb.Client()


# %%
# Create a collection
collection = chroma_client.create_collection(name="my_collection")


# %%
# Add some text documents to the collection
collection.add(
    ids=["id1", "id2"],
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ]
)


# %%
# Query the collection
results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)

print(results)
# # output: 
# {
#     'ids': [['id1', 'id2']], 
#     'embeddings': None, 
#     'documents': [[
#         'This is a document about pineapple', 
#         'This is a document about oranges'
#     ]], 
#     'uris': None, 
#     'included': ['metadatas', 'documents', 'distances'], 
#     'data': None, 
#     'metadatas': [[None, None]], 
#     'distances': [[1.0404009819030762, 1.2430799007415771]]
# }


# %%
