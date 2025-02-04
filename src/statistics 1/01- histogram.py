# Import necessary libraries
import os  # For working with file paths
import pandas as pd  # For data manipulation and loading
import matplotlib.pyplot as plt  # For creating plots

# Set the working directory to the location of the script
# Assuming the dataset is located in a 'data' folder two levels up from this script
# This ensures portability across different environments
data_folder = os.path.join(os.path.dirname(__file__),
                            '..', '..', 'data')  # Navigate to the data folder
data_file = os.path.join(data_folder, 'CTQ2-1.CSV')  # Full path to the CSV file

# Load the dataset
# Use pandas to read the CSV file
# The 'na_values' parameter replaces "NA" strings in the dataset with NaN (missing values)
dataset = pd.read_csv(data_file, na_values="NA")

# Set the Y measures (columns 3 to 5) and produce a histogram for each
# In Python, columns are zero-indexed, so column 3 to 5 in R corresponds to index 2 to 4 in Python
for y_col in dataset.columns[2:5]:  # Iterate through the specified columns
    plt.figure(figsize=(8, 6))  # Create a new figure with a specified size
    dataset[y_col].hist(  # Generate a histogram for the current column
        bins=30,  # Set the number of bins (bars) in the histogram
        color="#0000DD",  # Set the bar color to blue
        edgecolor="black",  # Set the edge color for better visibility
        density=True  # Normalize the histogram to show density instead of counts
    )
    plt.title(f"Histogram of {y_col}")  # Set the title of the plot dynamically
    plt.xlabel("Wait Time")  # Label the x-axis
    plt.ylabel("Density")  # Label the y-axis
    plt.axvline(x=20, color='red', linestyle='--', linewidth=2, label='Target = 20')
    # Add a vertical line at x=20 (target value) for reference
    plt.legend()  # Add a legend to the plot
    plt.show()  # Display the plot

# Optional: Create a single figure with harmonized x-axis for all histograms
# This section combines all histograms into a single figure with multiple subplots
plt.figure(figsize=(8, 12))  # Set the figure size for the combined plot
for idx, y_col in enumerate(dataset.columns[2:5], start=1):  # Loop with index for subplot placement
    plt.subplot(3, 1, idx)  # Create a subplot (3 rows, 1 column, current position idx)
    dataset[y_col].hist(  # Generate the histogram
        bins=30,  # Same bin settings for consistency
        color="#0000DD",  # Bar color
        edgecolor="black",  # Edge color
        density=True  # Normalize for density
    )
    plt.title(f"Histogram of {y_col}")  # Dynamic title for each plot
    plt.axvline(x=20, color='red', linestyle='--', linewidth=2, label='Target = 20')
    # Add the same reference line
    plt.legend()  # Add a legend for each subplot
    plt.tight_layout()  # Adjust layout to prevent overlap of subplots

plt.show()  # Display the combined plot
