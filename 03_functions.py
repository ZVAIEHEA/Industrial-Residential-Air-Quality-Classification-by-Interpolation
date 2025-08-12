import numpy as np
import matplotlib.pyplot as plt

def interpolate_vandermonde(dataset) :
  coefficients_list = []
  for index, row in dataset.iterrows():    
    x = dataset['CO'].values
    y = dataset['PM10'].values
    n = len(x)
    A = np.vander(x, increasing=True)
    regularization_term = 1e-10  
    A += np.eye(A.shape[0]) * regularization_term
    coefficients = np.linalg.solve(A, y)
    coefficients_list.append(coefficients)
    return coefficients_list


def draw_interpolation(coefficients_list):
  # Implement the drawing of the interpolation


  # Generate x values
  x = np.linspace(0, 50, 500)  # Adjust range as needed

  # Evaluate the polynomial using the coefficients
  y1 = np.polyval(coefficients_list[0], x)
  y2 = np.polyval(coefficients_list[0], x)


  # Create the plot
  plt.figure(figsize=(10, 6))
  plt.plot(x, y1, label='Polynomial Interpolation 1', color='blue')
  plt.plot(x, y2, label='Polynomial Interpolation 2', color='green')
  plt.xlabel('CO')
  plt.ylabel('PM10')
  plt.title('Polynomial Interpolation of PM10 vs CO')

  # Add data points
  #plt.scatter(dataset['CO'], dataset['PM10'], color='red', label='Data Points')

  plt.legend()
  plt.grid(True)
  plt.show()
  