import numpy as np
import matplotlib.pyplot as plt

def interpolate_vandermonde(dataset) :
    x = dataset['CO'].values
    y = dataset['PM10'].values
    n = len(x)
    A = np.vander(x, increasing=True)
    regularization_term = 1e-10  
    A += np.eye(A.shape[0]) * regularization_term
    coefficients = np.linalg.solve(A, y)
    return coefficients

