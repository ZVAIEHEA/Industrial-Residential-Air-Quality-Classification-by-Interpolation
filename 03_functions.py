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


def draw_interpolation(coefficients, dataset, city_name):
  # Generate x values for smooth curve
  x_min, x_max = dataset['CO'].min(), dataset['CO'].max()
  x = np.linspace(x_min - 5, x_max + 5, 500)

  # Evaluate the polynomial using the coefficients (reverse for polyval)
  y = np.polyval(coefficients[::-1], x)

  # Create the plot
  plt.figure(figsize=(10, 6))
  plt.plot(x, y, label=f'{city_name} Polynomial Interpolation', linewidth=2)
  
  # Add data points
  plt.scatter(dataset['CO'], dataset['PM10'], color='red', s=100, label='Data Points', zorder=5)
  
  plt.xlabel('CO')
  plt.ylabel('PM10')
  plt.title(f'Polynomial Interpolation of PM10 vs CO - {city_name}')
  plt.legend()
  plt.grid(True)
  plt.show()
  