import numpy as np

from mgen.rotation_matrix_3d import random_rotation

# Generate a bunch of random matrices to analyse its statistical properties
n2 = 100
nx = 100
x = 6

r2 = np.array([random_rotation(2) for _ in range(n2)])
rx = np.array([random_rotation(x) for _ in range(nx)])

# vectors with length one ...
vec2 = np.array([1.0,0.0])
vecx = np.zeros(x, dtype=np.float64)
vecx[0] = 1.0

# ... should keep length one ...
rot2 = np.matmul(r2,vec2)
rotx = np.matmul(rx,vecx)

lengths2 = np.sum(rot2*rot2, axis=1)
lengthsx = np.sum(rotx*rotx, axis=1)

print("Minimum length: %.5f; Maximum length: %.5f"%(np.amin(lengths2),np.amax(lengths2)))
print("Minimum length: %.5f; Maximum length: %.5f"%(np.amin(lengthsx),np.amax(lengthsx)))

# Lets take a look at the distribution of some rotated vectors in 2d
import matplotlib as mpl
mpl.use("agg")
import matplotlib.pyplot as plt

plt.close("all")
fig = plt.figure(figsize=(4.8,4.8), dpi=120)
plt.scatter(r2[:,0], r2[:,1], s=1)
plt.savefig("random_2d_vectors.png")