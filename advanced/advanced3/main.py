import numpy as np

a = np.arange(16).reshape(2, 2, 2, 2)

print(a[..., 0].flatten())
print(a[:, :, :, 0].flatten())