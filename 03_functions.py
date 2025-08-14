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


def regression_function(dataset_Zurich_sample, zurich_coefficients):
    # Create the coefficients of the polynomial function
    polynomial_coefficients = zurich_coefficients

    # Define the boundaries for the regression function
    min_co = dataset_Zurich_sample['CO'].min()
    max_co = dataset_Zurich_sample['CO'].max()
    min_co = int(min_co)
    max_co = int(max_co)

    # Create the regression function

    for x in range(min_co, max_co):
        polynomial_function = np.polyval(polynomial_coefficients[::-1], x)
        