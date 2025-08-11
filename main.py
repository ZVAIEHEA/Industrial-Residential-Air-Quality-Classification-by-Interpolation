import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_openml

# Fetch the dataset
try:
    housing = fetch_openml(name="house-prices-2", as_frame=True)
    df = housing.frame
except Exception as e:
    print(f"Error fetching dataset: {e}")
    exit()

# Data Cleaning and Preparation
if df is not None:
    # Fill missing values (replace with median for numerical columns)
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].median())
        else:
            # For simplicity, fill categorical with mode.  Consider more sophisticated handling in real application.
            df[col] = df[col].fillna(df[col].mode()[0])

    # Feature Engineering: Price per square meter (assuming 'SalePrice' is total price and 'GrLivArea' is living area in sq ft)
    df['PricePerSqM'] = df['SalePrice'] / (df['GrLivArea'] * 0.092903) # Convert sq ft to sq meters

    # Chicago neighborhood data might not be directly available.  Using 'Neighborhood' feature as a proxy.
    # Real world:  Would require mapping 'Neighborhood' or lat/lon to Chicago neighborhood definitions.

    # Group by neighborhood and calculate the median price per square meter
    neighborhood_prices = df.groupby('Neighborhood')['PricePerSqM'].median().sort_values()

    # Plotting
    plt.figure(figsize=(12, 8))  # Adjust figure size for better readability
    neighborhood_prices.plot(kind='bar')
    plt.title('Median House Price per Square Meter in Chicago (by Neighborhood Proxy)')
    plt.xlabel('Neighborhood')
    plt.ylabel('Median Price per Square Meter')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.show()
else:
    print("Failed to load the dataset. Cannot create the plot.")