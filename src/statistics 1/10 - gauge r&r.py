# Import necessary libraries
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #py -m pip install scikit-learn

""" # Note: Gage R&R study is often carried out using specialized software like Minitab or Six Sigma tools. Below, we simplify the R code using Python with a basic approach.

# Set the number of operators, parts, and measurements
operators = 3
parts = 10
measurements = 3

# Step 1: Create the experimental design as a dataframe
np.random.seed(42)  # for reproducibility

# Generate design with random parts, operators, and measurements
design = {
    'Operator': np.repeat(np.arange(1, operators + 1), parts * measurements),
    'Part': np.tile(np.repeat(np.arange(1, parts + 1), measurements), operators),
    'Measurement': np.nan  # placeholder for actual measurement values
}
design_df = pd.DataFrame(design)

# Step 2: Export the experimental design to CSV for data entry
datafile = "GRR_JTS.csv"
design_df.to_csv(datafile, index=False)
print(f"Experimental design saved to {datafile} for data capture.") """

# Step 3: Assume the measurements are recorded in the same CSV file after the experiment
# Load the dataset from the uploaded file for Gage R&R Analysis

data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')  # Navigate to the data folder
data_file = os.path.join(data_folder, 'GRR JTS COMPLETE.csv')  # Full path to the CSV file
dataset = pd.read_csv(data_file)

# Assuming the dataset has 'Operator', 'Part', and 'Measurement' columns
# Step 4: Perform a simple Gage R&R Analysis

# Extract relevant columns
design_df = dataset[['Operator', 'Part', 'Measurement']]

# Extract measurement data from the dataset
design_df['Measurement'] = dataset['Measurement']

# Assuming the dataset has 'Operator', 'Part', and 'Measurement' columns
# Step 4: Perform a simple Gage R&R Analysis

# Extract relevant columns
design_df = dataset[['Operator', 'Part', 'Measurement']]

# Calculate the mean for each part/operator combination
part_operator_mean = design_df.groupby(['Part', 'Operator'])['Measurement'].mean().unstack()
part_mean = design_df.groupby('Part')['Measurement'].mean()
operator_mean = design_df.groupby('Operator')['Measurement'].mean()

total_mean = design_df['Measurement'].mean()

# Calculate Repeatability and Reproducibility metrics
repeatability = design_df.groupby(['Part', 'Operator'])['Measurement'].std().mean()  # Within part/operator variation
reproducibility = operator_mean.std()  # Variation between operators

# Calculate Part-to-Part variation
part_to_part_variation = part_mean.std()  # Variation between parts

# Calculate Total Gage R&R
total_gage_rr = np.sqrt(repeatability**2 + reproducibility**2)

# Calculate Total Variation
total_variation = np.sqrt(repeatability**2 + reproducibility**2 + part_to_part_variation**2)

# Contribution percentages
repeatability_percent = (repeatability**2 / total_variation**2) * 100
reproducibility_percent = (reproducibility**2 / total_variation**2) * 100
part_to_part_percent = (part_to_part_variation**2 / total_variation**2) * 100
total_gage_rr_percent = (total_gage_rr**2 / total_variation**2) * 100

# Output a detailed summary
print("Gage R&R Analysis Summary:")
print(f"Overall Mean: {total_mean:.2f}")
print(f"Repeatability (within part/operator): {repeatability:.2f}")
print(f"Reproducibility (between operators): {reproducibility:.2f}")
print(f"Part-to-Part Variation: {part_to_part_variation:.2f}")
print(f"Total Gage R&R: {total_gage_rr:.2f}")
print(f"Total Variation: {total_variation:.2f}")
print("\n% Contribution:")
print(f"Repeatability: {repeatability_percent:.2f}%")
print(f"Reproducibility: {reproducibility_percent:.2f}%")
print(f"Part-to-Part: {part_to_part_percent:.2f}%")
print(f"Total Gage R&R: {total_gage_rr_percent:.2f}%")

# Flagging the result of the study based on criteria
if total_gage_rr_percent < 10:
    flag_message = "The measurement system is considered acceptable and very precise."
elif 10 <= total_gage_rr_percent <= 30:
    flag_message = "The measurement system is acceptable depending on other factors, such as the cost of the measuring device or the importance of the characteristics."
else:
    flag_message = "The measurement system is unacceptable and needs improvement. This could be due to high equipment variability, meaning there are significant differences between measurements of the same part."

print(f"\nResult Flag: {flag_message}")

# Step 5: Plotting results to visualize the variance
plt.figure(figsize=(10, 6))
plt.boxplot([design_df[design_df['Operator'] == i]['Measurement'] for i in design_df['Operator'].unique()],
            labels=[f'Operator {i}' for i in design_df['Operator'].unique()])
plt.title('Measurement Variation by Operator')
plt.xlabel('Operator')
plt.ylabel('Measurement')
plt.show()

# Additional visualization: % Contribution bar chart
plt.figure(figsize=(10, 6))
contributions = [repeatability_percent, reproducibility_percent, part_to_part_percent, total_gage_rr_percent]
labels = ['Repeatability', 'Reproducibility', 'Part-to-Part', 'Total Gage R&R']
plt.bar(labels, contributions, color='skyblue')
plt.title('% Contribution to Total Variation')
plt.xlabel('Source of Variation')
plt.ylabel('% Contribution')
plt.ylim(0, 100)
plt.show()