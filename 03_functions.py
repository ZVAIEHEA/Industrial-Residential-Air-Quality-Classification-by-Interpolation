import numpy as np

def interpolate_vandermonde(dataset) :
  coefficients_list = []
  for index, row in dataset.iterrows():    
    x = dataset['CO'].values
    y = dataset['PM10'].values
    n = len(x)
    A = np.vander(x, increasing=True)
    coefficients = np.linalg.solve(A, y)
    coefficients_list.append(coefficients)
    return coefficients_list


