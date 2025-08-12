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

if __name__ == "__main__" :
  # Load the dataset
  dataset = pd.read_csv('City_Types.csv')
  print(dataset.columns.values.tolist())

  # Get the data
  dataset_Zurich_sample, dataset_Beijing_sample = get_data(dataset)
  
  # Interpolate the functions from the data
  zurich_coefficients = interpolate_vandermonde(dataset_Zurich_sample)
  beijing_coefficients = interpolate_vandermonde(dataset_Beijing_sample)
  print("Zurich Coefficients:", zurich_coefficients)
  print("Beijing Coefficients:", beijing_coefficients)

  # In last part so the code can run
  draw_data(dataset_Zurich_sample, dataset_Beijing_sample)


