import numpy as np


x = np.arange(1, 11)
print(f'x = {x}')
y = 2 * x + np.random.randn(10)*2
print(f'y = {y}')
X = np.vstack((x,y))
print(X)
Xcentered = (X[0] - x.mean(), X[1] - y.mean())
m = (x.mean(), y.mean())
print(f'Xcentered = {Xcentered}')
print(f'Mean vector: {m}')
covmat = np.cov(Xcentered)
print(covmat, "\n")
print("Variance of X: ", np.cov(Xcentered)[0,0])
print("Variance of Y: ", np.cov(Xcentered)[1,1])
print("Covariance X and Y: ", np.cov(Xcentered)[0,1])
