############################
## MNIST
############################


# %%
# download MNIST dataset at OpenML.org
from sklearn.datasets import fetch_openml   # fetch_*(): download dataset, load_*(): load small size dataset, make_*(): fake dataset

mnist = fetch_openml('mnist_784', as_frame=False)
# output: RemoteDisconnected: Remote end close connection without response


# %%
