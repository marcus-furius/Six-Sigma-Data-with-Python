# Explanation: This script loads a dataset, selects variables for analysis, visualizes their relationship with a scatter plot, and calculates the correlation coefficient.

# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For creating visualizations
import numpy as np  # For mathematical operations like correlation calculation
import os

# Load the data
# Replace the file path with the appropriate path to your CSV file
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'VOLUME2.CSV')
dataset = pd.read_csv(data_file, na_values="NA")

# Set the x and y variables
x = dataset['BirmVol']  # Independent variable
y = dataset['Birm']     # Dependent variable

# Simple scatter plot: y against x
plt.figure(figsize=(8, 6))  # Set the size of the plot
plt.scatter(x, y, alpha=0.7)
plt.xlabel('Call Volume')  # Label for the x-axis
plt.ylabel('Wait Time')    # Label for the y-axis
plt.title('Scatter Plot of Wait Time vs Call Volume')  # Plot title
plt.show()

# Calculate the correlation coefficient (r value)
r_value = round(np.corrcoef(x[~x.isna() & ~y.isna()], y[~x.isna() & ~y.isna()])[0, 1], 2)

# Customized scatter plot with r value
plt.figure(figsize=(8, 6))  # Set the size of the plot
plt.scatter(x, y, alpha=0.7, color='blue', edgecolor='black', s=50)  # Create the scatter plot
plt.xlabel('Call Volume')  # Label for the x-axis
plt.ylabel('Wait Time')    # Label for the y-axis
plt.title('Searching Correlation between Call Volume and Wait Time')  # Main title
plt.figtext(0.5, 0.01, f"r value = {r_value}", ha="center", fontsize=10, color="black")  # Add the r value as a subtitle
plt.grid(alpha=0.3)  # Optional: Add a grid for better readability
plt.show()
