import importlib
import pandas as pd
import matplotlib.pyplot as plt

# Import modules using importlib
data_module = importlib.import_module('02_data')
functions_module = importlib.import_module('03_functions')

# Extract functions from modules
get_data = data_module.get_data
draw_data = data_module.draw_data
interpolate_vandermonde = functions_module.interpolate_vandermonde
regression_function = functions_module.regression_function

if __name__ == "__main__" :
  # Load the dataset
  dataset = pd.read_csv('City_Types.csv')
  #print(dataset.columns.values.tolist())

  # Get the data
  dataset_Zurich_sample = get_data(dataset)
  print("Zurich Sample:", dataset_Zurich_sample)
  
  # Interpolate the functions from the data
  zurich_coefficients = interpolate_vandermonde(dataset_Zurich_sample)
  print("Zurich Coefficients:", zurich_coefficients)


  # Regression function
  zurich_regression_function = regression_function(dataset_Zurich_sample, zurich_coefficients)
  print("Zurich Regression Function:", zurich_regression_function)
  
  # In last part so the code can run
  draw_data(dataset_Zurich_sample, zurich_coefficients)
  


