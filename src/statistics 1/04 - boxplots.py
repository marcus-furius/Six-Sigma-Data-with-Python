# Explanation: This script creates various box plots from a dataset, including single box plots, grouped box plots, and multi-panel box plots with consistent scaling.

# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import matplotlib.pyplot as plt  # For creating visualizations
import os

# Load the data
# Replace the file path with the appropriate path to your CSV file
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'CTQ2-1.CSV')

# Load the dataset directly (since we have the content)
# Specify parse_dates to properly handle the date column
dataset = pd.read_csv(data_file, 
                     parse_dates=['Date'],  # Convert Date column to datetime
                     na_values=["", "NA"])  # Handle both empty cells and "NA" as missing values

# Clean the data by removing rows where all relevant columns (Birm, Cov, Av) are missing
dataset = dataset.dropna(subset=['Birm', 'Cov', 'Av'], how='all')

# 1. Create a simple box plot for the 'Av' column
plt.figure(figsize=(10, 6))
plt.boxplot(dataset['Av'].dropna())  # dropna() removes any remaining NaN values
plt.title("Boxplot of Av")
plt.ylabel("Value")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 2. Create a boxplot for Av grouped by Day
plt.figure(figsize=(12, 6))
# Create the boxplot with cleaned data
dataset.boxplot(column='Av', by='Day', figsize=(12, 6))
plt.title("Boxplot of Av by Day")
plt.suptitle('')  # Remove the automatic suptitle
plt.ylabel("Value")
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# 3. Create boxplots for Birm, Cov, and Av
# First, create a 2x2 subplot layout
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
axes = axes.ravel()  # Flatten the 2x2 array to make it easier to iterate

# Get the columns we want to plot (Birm, Cov, Av)
columns_to_plot = ['Birm', 'Cov', 'Av']

# Create boxplots for each column
for idx, column in enumerate(columns_to_plot):
    # Create boxplot on the corresponding subplot
    dataset.boxplot(column=column, by='Day', ax=axes[idx])
    axes[idx].set_title(f"Boxplot of {column}")
    axes[idx].set_ylim(0, 70)  # Set y-axis limits
    axes[idx].grid(True, linestyle='--', alpha=0.7)
    axes[idx].set_ylabel("Value")

# Remove the empty fourth subplot
fig.delaxes(axes[3])

plt.tight_layout()  # Adjust subplot layout
plt.show()

# 4. Create boxplots with custom day ordering
# Define the custom order for days
day_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

# Convert Day column to categorical with specific order
dataset['Day'] = pd.Categorical(dataset['Day'], categories=day_order, ordered=True)

# Create the final plot with ordered days
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
axes = axes.ravel()

for idx, column in enumerate(columns_to_plot):
    # Create boxplot with ordered days
    dataset.boxplot(column=column, by='Day', ax=axes[idx])
    axes[idx].set_title(f"Boxplot of {column}")
    axes[idx].set_ylim(0, 70)
    axes[idx].grid(True, linestyle='--', alpha=0.7)
    axes[idx].set_ylabel("Value")

# Remove the empty fourth subplot
fig.delaxes(axes[3])

plt.tight_layout()
plt.show()

# Optional: Print summary statistics for verification
print("\nSummary statistics for Av grouped by Day:")
print(dataset.groupby('Day')['Av'].describe())