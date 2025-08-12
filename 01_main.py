from importlib import reload
import pandas as pd


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


