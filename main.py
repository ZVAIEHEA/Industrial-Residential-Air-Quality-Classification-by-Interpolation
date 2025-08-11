
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Fetch the Titanic dataset for binary classification
try:
    titanic = fetch_openml(name="titanic", version=1, as_frame=True)
    df = titanic.frame
    print("Dataset loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    print(f"Target variable: survival (0 = died, 1 = survived)")
except Exception as e:
    print(f"Error fetching dataset: {e}")
    exit()

# Data Cleaning and Preparation
if df is not None:
    # Display basic info about the dataset
    print("\nDataset Info:")
    print(df.head())
    print(f"\nTarget distribution:")
    print(df['survived'].value_counts())
    
    # Handle missing values
    df['age'] = df['age'].fillna(df['age'].median())
    df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
    
    # Convert categorical variables to numeric
    df['sex_numeric'] = df['sex'].map({'male': 1, 'female': 0})
    df['embarked_numeric'] = df['embarked'].map({'S': 0, 'C': 1, 'Q': 2})
    
    # Select features for classification
    features = ['pclass', 'sex_numeric', 'age', 'sibsp', 'parch', 'fare', 'embarked_numeric']
    X = df[features].fillna(0)  # Fill any remaining NaN values
    y = df['survived']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a logistic regression model
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Accuracy: {accuracy:.3f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Visualizations
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. Survival by Gender
    survival_by_sex = df.groupby('sex')['survived'].mean()
    survival_by_sex.plot(kind='bar', ax=ax1, color=['pink', 'lightblue'])
    ax1.set_title('Survival Rate by Gender')
    ax1.set_ylabel('Survival Rate')
    ax1.set_xlabel('Gender')
    ax1.tick_params(axis='x', rotation=0)
    
    # 2. Survival by Passenger Class
    survival_by_class = df.groupby('pclass')['survived'].mean()
    survival_by_class.plot(kind='bar', ax=ax2, color='lightgreen')
    ax2.set_title('Survival Rate by Passenger Class')
    ax2.set_ylabel('Survival Rate')
    ax2.set_xlabel('Passenger Class')
    ax2.tick_params(axis='x', rotation=0)
    
    # 3. Age distribution by survival
    survived = df[df['survived'] == 1]['age'].dropna()
    died = df[df['survived'] == 0]['age'].dropna()
    ax3.hist([died, survived], bins=20, label=['Died', 'Survived'], 
             alpha=0.7, color=['red', 'green'])
    ax3.set_title('Age Distribution by Survival')
    ax3.set_xlabel('Age')
    ax3.set_ylabel('Frequency')
    ax3.legend()
    
    # 4. Feature importance
    feature_importance = abs(model.coef_[0])
    feature_names = features
    importance_df = pd.DataFrame({
        'feature': feature_names,
        'importance': feature_importance
    }).sort_values('importance', ascending=True)
    
    importance_df.plot(x='feature', y='importance', kind='barh', ax=ax4, color='orange')
    ax4.set_title('Feature Importance in Logistic Regression')
    ax4.set_xlabel('Absolute Coefficient Value')
    
    plt.tight_layout()
    plt.show()
    
    # Print some insights
    print(f"\nKey Insights:")
    print(f"- Overall survival rate: {df['survived'].mean():.1%}")
    print(f"- Female survival rate: {df[df['sex'] == 'female']['survived'].mean():.1%}")
    print(f"- Male survival rate: {df[df['sex'] == 'male']['survived'].mean():.1%}")
    print(f"- First class survival rate: {df[df['pclass'] == 1]['survived'].mean():.1%}")
    print(f"- Third class survival rate: {df[df['pclass'] == 3]['survived'].mean():.1%}")
    
else:
    print("Failed to load the dataset. Cannot create the analysis.")
