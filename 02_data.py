import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Force TkAgg backend for VNC
import matplotlib.pyplot as plt
import numpy as np

def get_data(dataset):

  # Filter the dataset for the specific cities and types
  dataset_Zurich = dataset[dataset['Type'].isin(['Industrial'])]
  dataset_Zurich = dataset[dataset['City'].isin(['Zurich'])]
  #dataset_Beijing = dataset[dataset['Type'].isin(['Industrial'])]
  #dataset_Beijing = dataset[dataset['City'].isin(['Beijing'])]

  #print(dataset_Beijing)

  # Sample 6 random rows from the filtered datasets
  dataset_Zurich_sample = dataset_Zurich.sample(n=6)[['CO','PM10']]
  #dataset_Beijing_sample = dataset_Beijing.sample(n=6)[['CO','PM10']]

  #print(dataset_Zurich_sample)
  #print(dataset_Beijing_sample)


  return dataset_Zurich_sample


def draw_data(dataset_Zurich_sample, zurich_coefficients):
  
  # Debug: Print the actual data values
  print("Zurich CO values:", dataset_Zurich_sample['CO'].values)
  print("Zurich PM10 values:", dataset_Zurich_sample['PM10'].values)
  #print("Beijing CO values:", dataset_Beijing_sample['CO'].values)
  #print("Beijing PM10 values:", dataset_Beijing_sample['PM10'].values)
  
  # Plot the data points   
  plt.figure(figsize=(8, 6))
  plt.scatter(dataset_Zurich_sample['CO'], dataset_Zurich_sample['PM10'], marker='o', color='blue', label='Zurich')
  #plt.scatter(dataset_Beijing_sample['CO'], dataset_Beijing_sample['PM10'], marker='x', color='red', label='Beijing')
  plt.xlabel('CO')
  plt.ylabel('PM10')
  plt.title('CO vs PM10 for Zurich and Beijing (Industrial)')
  
  # Plot the interpolated functions - Fix the np.linspace syntax
  min_co = dataset_Zurich_sample['CO'].min()
  max_co = dataset_Zurich_sample['CO'].max()
  x = np.linspace(min_co, max_co, 100)
  plt.plot(x, np.polyval(zurich_coefficients[::-1], x), color='blue', linestyle='--', label='Zurich Interpolation')
  #plt.plot(x, np.polyval(beijing_coefficients[::-1], x), color='red', linestyle='--', label='Beijing Interpolation')
  #plt.plot(x, np.polyval(classification_coefficients[::-1], x), color='green', linestyle='--', label='Classification Function')
  
  # Set explicit axis limits
  plt.xlim(min_co - 50, max_co + 50)
  all_pm10 = np.concatenate([dataset_Zurich_sample['PM10'].values])
  plt.ylim(all_pm10.min() - 10, all_pm10.max() + 10)
  
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.draw()
  plt.pause(0.1)  # Force display refresh
  plt.show()
  input("Appuyez sur Entrée pour continuer...")  # Keep window open
