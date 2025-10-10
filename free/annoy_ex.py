from annoy import AnnoyIndex
import random


dimension = 40  # vector dimension
n_trees = 10    
index = AnnoyIndex(dimension, 'euclidean')  # f: int(dimension=40), metric('euclidean')

# add data
for i in range(1000):
    vector = [random.gauss(0, 1) for z in range(dimension)] # gaussian distribution -> mu: 0(float), sigma: standart deviation
    index.add_item(i, vector)

index.build(n_trees)

# query vector
query_vector = [random.gauss(0, 1) for z in range(dimension)]

# search nearest neighbors
nearest_neighbors = index.get_nns_by_vector(query_vector, 5, include_distances=True)

print("Nearest neighbors: ", nearest_neighbors) # tuple[list[int], list[float]]
# # output: 
# Nearest neighbors:  ([201, 233, 98, 465, 371], [6.035238265991211, 6.163309097290039, 6.227492809295654, 6.451484680175781, 6.539395809173584])
