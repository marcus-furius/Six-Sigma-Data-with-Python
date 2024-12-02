import pandas as pd
import os

# Load the data
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')  # Navigate to the data folder
data_file = os.path.join(data_folder, 'ERRORS.CSV')  # Full path to the CSV file

# Load the dataset
# Use pandas to read the CSV file
# The 'na_values' parameter replaces "NA" strings in the dataset with NaN (missing values)
dataset = pd.read_csv(data_file, na_values="NA")

# Display summary statistics for columns 2 and 3 (assumed 0-based indexing for Python)
print(dataset.iloc[:, 1:3].describe(include='all'))

# Cross tabulate the data from columns 2 and 3
crosstab_result = pd.crosstab(dataset.iloc[:, 1], dataset.iloc[:, 2])
print(crosstab_result)

# Convert the crosstab result into a DataFrame for further analysis if needed
datatable = crosstab_result.reset_index()

# Save the analysis
datatable.to_csv(os.path.join(data_folder, 'analysis_results.csv'))