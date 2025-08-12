import pandas as pd
import matplotlib.pyplot as plt


def get_data(dataset):


  dataset_Zurich = dataset[dataset['Type'].isin(['Industrial'])]
  dataset_Zurich = dataset[dataset['City'].isin(['Zurich'])]
  dataset_Beijing = dataset[dataset['Type'].isin(['Industrial'])]
  dataset_Beijing = dataset[dataset['City'].isin(['Beijing'])]

  #print(dataset_Beijing)

  
  dataset_Zurich_sample = dataset_Zurich.sample(n=6)[['CO','PM10']]
  dataset_Beijing_sample = dataset_Beijing.sample(n=6)[['CO','PM10']]

  return dataset_Zurich_sample, dataset_Beijing_sample

def draw_data(dataset_Zurich_sample, dataset_Beijing_sample) :
  plt.figure(figsize=(8, 6))
  plt.scatter(dataset_Zurich_sample['CO'], dataset_Zurich_sample['PM10'], marker='o', color='blue', label='Zurich')
  plt.scatter(dataset_Beijing_sample['CO'], dataset_Beijing_sample['PM10'], marker='x', color='red', label='Beijing')
  plt.xlabel('CO')
  plt.ylabel('NO2')
  plt.title('CO vs NO2 for Zurich and Beijing (Industrial)')
  plt.legend()
  plt.grid(True)
  plt.show()

def interpolate_vandermonde(dataset_Zurich_sample, dataset_Beijing_sample) :
  a=1
  return a


if __name__ == "__main__" :
  print("Hello World")
  dataset = pd.read_csv('City_Types.csv')
  print(dataset.columns.values.tolist())
  dataset_Zurich_sample, dataset_Beijing_sample = get_data(dataset)
  draw_data(dataset_Zurich_sample, dataset_Beijing_sample)
  
