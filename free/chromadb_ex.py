# %%
import pickle 
import chromadb
import random
import pandas
import pandas as pd
import numpy as np
import cupy as cp

from pathlib import Path
from PIL import Image


# %%
# load LFW Vector Embedding Dataset
with open('lfw_face_dataset', 'rb') as file:
    df = pickle.load(file)

# check data
df.tail()


# %%
# generate Chroma Client
client = chromadb.PersistentClient(path='chromadb')


# %%
# generate collection
collection = client.get_or_create_collection(
    name='lfw_faces',
    metadata={'hnsw:space', 'cosine'}
)

# get collection
collection.get()


# %%
# add to collection
for i in range(len(df)):
    row = df.iloc[i]
    face_name = row['name']
    face_path = row['path']
    face_id = Path(face_path).stem
    face_embedding = row['embedding']

    collection.add(
        embeddings=[face_embedding],
        metadatas=[{
            'name': face_name,
            'path': face_path
        }],
        ids=[face_id]
    )


# %%
rand_num = random.randint(0, len(df))
test_emb = df.iloc[rand_num]['embedding']
test_id = df.iloc[rand_num]['path']
print(f"rand_num: {rand_num}, id: {test_id}")


# %%
query_result = collection.query(
    query_embeddings=[test_emb],
    n_results=1
)


# %%
%%timeit 
query_result = collection.query(
    query_embeddings=[test_emb],
    n_results=1
)


# %%
%%timeit
query_result = collection.query(
    query_embeddings=[test_emb],
    n_results=5
)


# %%
%%timeit 
query_result = collection.query(
    query_embeddings=[test_emb],
    n_results=10
)


# %%
query_result


# %%
import torch 

def findCosineDistances(source_representation, test_representation_list, n=1):
    a = np.dot(source_representation, np.transpose(test_representation_list))   # (n,)
    b = np.sum(np.multiply(source_representation, source_representation))       # scalar
    c = np.sum(np.multiply(test_representation_list, test_representation_list), axis=1) # (n,)

    res_list = 1 - (a / (np.sqrt(b) * np.sqrt(c)))  # (n,)
    top_n_indexes = np.argsort(res_list)[::-1][:n]
    return res_list # numpy array

def find_top_n_nearest(source_representation, test_representation_list, n=1):
    a = np.dot(source_representation, np.transpose(test_representation_list))   # (n,)
    b = np.sum(np.multiply(source_representation, source_representation))       # scalar
    c = np.sum(np.multiply(test_representation_list, test_representation_list), axis=1) # (n,)

    res_list = 1 - (a / (np.sqrt(b) * np.sqrt(c)))  # (n,)
    top_n_indexes = np.argsort(res_list)[:n]
    return top_n_indexes