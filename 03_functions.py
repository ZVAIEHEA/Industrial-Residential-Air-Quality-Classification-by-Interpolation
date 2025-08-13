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


def classification_function(beijing_coefficients, zurich_coefficients):
    # Create the coefficients of the classification function
    a = float(0.5)
    b = float(0.5)
    c = float(2)
    beijing_coefficients = beijing_coefficients
    zurich_coefficients = zurich_coefficients
    raw_classification_coefficients = []
    for i in range(len(beijing_coefficients)):

        raw_classification_coefficients.append((a * beijing_coefficients[i] - b * zurich_coefficients[i]) / c)
    
    classification_coefficients = [float(value) for value in raw_classification_coefficients]
    
    print("Classification Coefficients:")

    
    print(classification_coefficients)
    print("33344")

    return classification_coefficients