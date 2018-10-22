import numpy as np
from scipy.stats import multivariate_normal as mvn
import matplotlib.pyplot as plt
D = 2
x = np.random.rand(D)
mu = np.random.rand(D)
A = np.random.rand(D,D)
# random symmetric matrix
cov = A.T.dot(A)

# Generate grid points
x, y = np.meshgrid(np.linspace(-1,2,100),np.linspace(-1,2,100))
xy = np.column_stack([x.flat, y.flat])

# density values at the grid points
Z = mvn.pdf(xy, mu, cov).reshape(x.shape)

# arbitrary contour levels
contour_level = [0.1, 0.2, 0.3]

fig = plt.contour(X, Y, Z, levels = contour_level)