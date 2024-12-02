# Explanation: This script reads a dataset, filters it based on certain conditions, and creates histograms for subsets of data grouped by unique days.

# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For creating visualizations
import os

# Load the data
# Replace the file path with the appropriate path to your CSV file
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'CTQ2-1.CSV')
dataset = pd.read_csv(data_file, na_values="NA")

# Subset 1: Rows where 'Cov' is less than or equal to 20
subset_data = dataset[dataset['Cov'] <= 20]

# Subset 2: Rows where 'Birm' is greater than 42 or less than 10
# This might indicate unusual data that needs investigation.
subset_data2 = dataset[(dataset['Birm'] > 42) | (dataset['Birm'] < 10)]

# Subset 3: Rows where 'Cov' is less than or equal to 20 and 'Day' equals 'Tuesday'
subset_data3 = dataset[(dataset['Cov'] <= 20) & (dataset['Day'] == "Tue")]

# Create histograms for each subset
plt.figure(figsize=(15, 5))

# Subplot for subset_data
plt.subplot(1, 3, 1)
plt.hist(subset_data['Cov'], bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.title('Subset 1: Cov <= 20')
plt.xlabel('Cov Value')
plt.ylabel('Frequency')

# Subplot for subset_data2
plt.subplot(1, 3, 2)
plt.hist(subset_data2['Birm'], bins=20, color='red', edgecolor='black', alpha=0.7)
plt.title('Subset 2: Birm > 42 or < 10')
plt.xlabel('Birm Value')
plt.ylabel('Frequency')

# Subplot for subset_data3
plt.subplot(1, 3, 3)
plt.hist(subset_data3['Cov'], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title('Subset 3: Cov <= 20 & Tuesday')
plt.xlabel('Cov Value')
plt.ylabel('Frequency')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

# Get unique values of 'Day'
days = dataset['Day'].unique()

# Save current plot settings
original_settings = plt.rcParams.copy()

# Set up a 3x3 grid for the plots
plt.figure(figsize=(15, 15))  # Define the size of the entire figure
plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Adjust space between subplots

# For each unique day, filter the dataset and create a histogram for 'Cov'
for i, day in enumerate(days, start=1):
    day_subset = dataset[dataset['Day'] == day]
    plt.subplot(3, 3, i)  # Create a subplot in the 3x3 grid
    plt.hist(day_subset['Cov'], bins=20, edgecolor='black', alpha=0.7)
    plt.title(f"Histogram for {day}")  # Set the title for the subplot
    plt.xlabel('Cov')  # Label for the x-axis
    plt.ylabel('Frequency')  # Label for the y-axis

# Show all histograms
plt.show()

# Restore original plot settings
plt.rcParams.update(original_settings)
