# Import required libraries
# Ensure you install matplotlib by running: `py -m pip install matplotlib` if not already installed
import os  # For working with file paths
import pandas as pd  # For data manipulation and loading
import matplotlib.pyplot as plt  # For creating plots

# Set working directory to the location of this script
# In Jupyter Notebooks or standalone scripts, you can use os.getcwd() to verify your current directory.
# Here, we assume the data is in the same directory as this script or adjust accordingly.
# Set the working directory to the location of the script
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'CTQ2-1.CSV')

# Load the dataset
# The dataset is assumed to be a CSV file, with headers, commas as separators, and possible "NA" values as missing.
dataset = pd.read_csv(data_file, na_values="NA")

# Define the columns for analysis (columns 3 to 5 in R are 2 to 4 in Python due to 0-based indexing)
columns_to_analyze = dataset.columns[2:5]

# Function to create a dot plot
# A dot plot can be approximated using matplotlib's scatter plot function
def create_dotplot(data, title, xlabel, xlim=None):
    """
    Create a dot plot for the given data.

    :param data: The data to plot (1D array or list)
    :param title: Title of the plot
    :param xlabel: Label for the x-axis
    :param xlim: Tuple for x-axis limits (optional)
    """
    rounded_data = data.round(0)  # Round data to the nearest whole number
    counts = rounded_data.value_counts().sort_index()  # Count unique values and sort by index

    # Scatter plot to mimic a dot plot
    for x, count in counts.items():
        plt.scatter([x] * count, range(1, count + 1), c='blue', alpha=0.6)

    plt.title(title)
    plt.xlabel(xlabel)
    if xlim:
        plt.xlim(xlim)
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for clarity
    plt.show()  # Display the plot

# Generate individual dot plots for each column
for column in columns_to_analyze:
    create_dotplot(
        dataset[column],
        title=f"Dot Plot of {column}",
        xlabel="Wait Time"
    )

# Save the current plotting parameters
# In Python, this is typically the default state
# Below, we modify the figure layout for combined plots
# Harmonize x-axis range for better comparison

# Create a figure with 3 rows and 1 column
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 12))  # Adjust size for readability

# Iterate through the columns and plot
for ax, column in zip(axes, columns_to_analyze):
    rounded_data = dataset[column].round(0)  # Round data
    counts = rounded_data.value_counts().sort_index()  # Count and sort

    # Scatter plot on specific subplot axes
    for x, count in counts.items():
        ax.scatter([x] * count, range(1, count + 1), c='blue', alpha=0.6)

    ax.set_title(f"Dot Plot of {column}")
    ax.set_xlabel("Wait Time")
    ax.set_xlim(0, 70)  # Harmonize the x-axis range
    ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust spacing to prevent overlap
plt.tight_layout()
plt.show()  # Display the combined plot
