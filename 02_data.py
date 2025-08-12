import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_data(dataset):

  # Filter the dataset for the specific cities and types
  dataset_Zurich = dataset[dataset['Type'].isin(['Industrial'])]
  dataset_Zurich = dataset[dataset['City'].isin(['Zurich'])]
  dataset_Beijing = dataset[dataset['Type'].isin(['Industrial'])]
  dataset_Beijing = dataset[dataset['City'].isin(['Beijing'])]

  #print(dataset_Beijing)

  # Sample 6 random rows from the filtered datasets
  dataset_Zurich_sample = dataset_Zurich.sample(n=6)[['CO','PM10']]
  dataset_Beijing_sample = dataset_Beijing.sample(n=6)[['CO','PM10']]

  #print(dataset_Zurich_sample)
  #print(dataset_Beijing_sample)


  return dataset_Zurich_sample, dataset_Beijing_sample


def draw_data(dataset_Zurich_sample, dataset_Beijing_sample, zurich_coefficients, beijing_coefficients):
  
  # Plot the data points   
  plt.figure(figsize=(8, 6))
  plt.scatter(dataset_Zurich_sample['CO'], dataset_Zurich_sample['PM10'], marker='o', color='blue', label='Zurich')
  plt.scatter(dataset_Beijing_sample['CO'], dataset_Beijing_sample['PM10'], marker='x', color='red', label='Beijing')
  plt.xlabel('CO')
  plt.ylabel('PM10')
  plt.title('CO vs PM10 for Zurich and Beijing (Industrial)')
  
  # Plot the interpolated functions
  x = np.linspace(1000,10000,1,2*dataset_Beijing_sample['CO'].max())
  plt.plot(x, np.polyval(zurich_coefficients, x), color='blue', linestyle='--', label='Zurich Interpolation')
  plt.plot(x, np.polyval(beijing_coefficients, x), color='red', linestyle='--', label='Beijing Interpolation')
  


  plt.legend()
  plt.grid(True)
  plt.show()
