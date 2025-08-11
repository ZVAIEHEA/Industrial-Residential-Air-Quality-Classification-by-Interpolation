import numpy as np

def vandermonde_interpolation(points, x) :
    n = len(points)
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    V = np.vander(x_coords, n, increasing=True)
    coeffs = np.linalg.solve(V, y_coords)
    return coeffs



def polynomial_functions(coeffs, x) :
    
    n = len(coeffs)
    result = 0
    for i in range(n):
        result += coeffs[i] * (x**i)
    return result
    