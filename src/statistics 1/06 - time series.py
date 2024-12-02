import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set the working directory to the current file's location
# Note: In Python, this is typically not necessary as we can use relative paths
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')  # Navigate to the data folder
data_file = os.path.join(data_folder, 'CTQ2-1.CSV')  # Full path to the CSV file

# Load the dataset
# Use pandas to read the CSV file
# The 'na_values' parameter replaces "NA" strings in the dataset with NaN (missing values)
dataset = pd.read_csv(data_file, na_values="NA")

# Extract our target variable
y = dataset['Av']

# Create Figure 1: Basic time series plot
plt.figure(figsize=(10, 6))  # Set figure size for better visibility
plt.plot(y, marker='o', linestyle='-', color='blue', 
         markersize=8, markerfacecolor='blue')
plt.ylabel('Av')
plt.title('Time Series Plot of Av')
plt.grid(True)  # Add grid for better readability
plt.show()

# Create Figure 2: Plot with highlighted outliers
plt.figure(figsize=(10, 6))
colors = ['red' if val < 10 else 'blue' for val in y]  # List comprehension for color mapping
plt.plot(y, marker='o', linestyle='-', color='blue', 
         markersize=8, markerfacecolor='blue')
plt.scatter(range(len(y)), y, c=colors, zorder=2)  # Overlay colored points
plt.ylabel('Av')
plt.title('Time Series Plot of Av (Outliers in Red)')
plt.grid(True)
plt.show()

# Create Figure 3: Advanced multi-line plot
plt.figure(figsize=(12, 6))

# Define plot colors
plot_colors = ['blue', 'red', 'forestgreen']

# Calculate maximum y value across all three columns
max_y = dataset[['Av', 'Birm', 'Cov']].max().max()

# Plot each series with different styles
plt.plot(dataset['Av'], marker='o', linestyle='-', 
         color=plot_colors[0], label='Av')
plt.plot(dataset['Birm'], marker='s', linestyle='--', 
         color=plot_colors[1], label='Birm')
plt.plot(dataset['Cov'], marker='D', linestyle=':', 
         color=plot_colors[2], label='Cov')

# Customize the plot
plt.xticks(range(len(dataset)), dataset['Date'], rotation=45)
plt.ylim(0, max_y)
plt.grid(True)
plt.title('Time Series Plot of Av, Birm and Cov')
plt.legend()
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()

# Create Figure 4: Side-by-side comparison plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Calculate maximum y value for consistent scaling
max_y = max(dataset['Birm'].max(), dataset['Cov'].max())

# Plot Birmingham data
ax1.plot(dataset['Birm'], marker='o', linestyle='-', 
         color='blue', markersize=6)
ax1.set_ylim(0, max_y)
ax1.set_ylabel('Birm')
ax1.set_title('Time Series Plot of Birm')
ax1.grid(True)

# Plot Coventry data
ax2.plot(dataset['Cov'], marker='o', linestyle='-', 
         color='blue', markersize=6)
ax2.set_ylim(0, max_y)
ax2.set_ylabel('Cov')
ax2.set_title('Time Series Plot of Cov')
ax2.grid(True)

plt.tight_layout()
plt.show()