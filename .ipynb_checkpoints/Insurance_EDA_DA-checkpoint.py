# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the dataset
file_path = r"C:\Users\Admin\Downloads\Data Analysis Using Python\Insurance\Insurance2.csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Display the first few rows of the dataset
print(df.head())

# Exploratory Data Analysis (EDA)

# Response Distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Response', data=df)
plt.title('Response Distribution')
plt.tight_layout()
plt.show()

# Gender Distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.tight_layout()
plt.show()

# Vehicle Age Distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Vehicle_Age', data=df)
plt.title('Vehicle Age Distribution')
plt.tight_layout()
plt.show()

# Vehicle Damage Distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Vehicle_Damage', data=df)
plt.title('Vehicle Damage Distribution')
plt.tight_layout()
plt.show()

# Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', kde=True)
plt.title('Age Distribution')
plt.tight_layout()
plt.show()

# Annual Premium Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Annual_Premium', kde=True)
plt.title('Annual Premium Distribution')
plt.tight_layout()
plt.show()

# Vintage Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Vintage', kde=True)
plt.title('Vintage Distribution')
plt.tight_layout()
plt.show()

# Bivariate Analysis

# Gender vs Response
plt.figure(figsize=(10, 6))
sns.barplot(x='Gender', y='Response', data=df)
plt.title('Gender vs Response')
plt.tight_layout()
plt.show()

# Vehicle Age vs Response
plt.figure(figsize=(10, 6))
sns.barplot(x='Vehicle_Age', y='Response', data=df)
plt.title('Vehicle Age vs Response')
plt.tight_layout()
plt.show()

# Vehicle Damage vs Response
plt.figure(figsize=(10, 6))
sns.barplot(x='Vehicle_Damage', y='Response', data=df)
plt.title('Vehicle Damage vs Response')
plt.tight_layout()
plt.show()

# Age Distribution by Response
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Response', kde=True)
plt.title('Age Distribution by Response')
plt.tight_layout()
plt.show()

# Annual Premium Distribution by Response
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Annual_Premium', hue='Response', kde=True)
plt.title('Annual Premium Distribution by Response')
plt.tight_layout()
plt.show()

# Pairplot of all features
sns.pairplot(df[features_for_rf + ['Response']], hue='Response')
plt.tight_layout()
plt.show()

# Additional Analysis: Response Rate by Age Group
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 20, 30, 40, 50, 60, 70, 100], labels=['0-20', '21-30', '31-40', '41-50', '51-60', '61-70', '70+'])
response_rate = df.groupby('Age_Group')['Response'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
response_rate.plot(kind='bar')
plt.title('Response Rate by Age Group')
plt.ylabel('Response Rate')
plt.tight_layout()
plt.show()

# Additional Analysis: Response Rate by Annual Premium Quartile
df['Premium_Quartile'] = pd.qcut(df['Annual_Premium'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
response_rate_premium = df.groupby('Premium_Quartile')['Response'].mean()
plt.figure(figsize=(10, 6))
response_rate_premium.plot(kind='bar')
plt.title('Response Rate by Annual Premium Quartile')
plt.ylabel('Response Rate')
plt.tight_layout()
plt.show()

print("Analysis completed successfully!")