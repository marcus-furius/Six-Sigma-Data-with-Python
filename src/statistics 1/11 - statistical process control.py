# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from statsmodels.stats.api import DescrStatsW

# Load the data
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')  # Navigate to the data folder
data_file = os.path.join(data_folder, 'RESOURCES.CSV')  # Full path to the CSV file

# Load the dataset
# Use pandas to read the CSV file
# The 'na_values' parameter replaces "NA" strings in the dataset with NaN (missing values)
dataset = pd.read_csv(data_file, na_values="NA")

# Prepare data for analysis
# We will use the 'Manufacturing.Defects' column
manufacturing_defects = dataset['Manufacturing Defects'].dropna()

# Plot Individuals Control Chart (X/mR Chart)
# Since Python doesn't have a direct equivalent of 'qcc', we will implement the logic for the Individual (I) Chart

# Calculate Moving Range (mR)
moving_range = manufacturing_defects.diff().abs().dropna()

# Calculate control limits and center line (mean)
x_bar = np.mean(manufacturing_defects)
mr_bar = np.mean(moving_range)

# Constants for calculating control limits for Individual Charts
# D4 and D3 are specific constants used for estimating control limits
D2 = 1.128  # Constant value for moving range of size 2
UCL = x_bar + (mr_bar / D2) * 3
LCL = x_bar - (mr_bar / D2) * 3

# Plot the Individuals Chart
plt.figure(figsize=(10, 6))
plt.plot(manufacturing_defects, marker='o', linestyle='-', color='b', label='Individual Values')
plt.axhline(y=x_bar, color='green', linestyle='-', linewidth=2, label='Center Line (Mean)')
plt.axhline(y=UCL, color='red', linestyle='--', linewidth=2, label='Upper Control Limit (UCL)')
plt.axhline(y=LCL, color='red', linestyle='--', linewidth=2, label='Lower Control Limit (LCL)')
plt.xlabel('Observations')
plt.ylabel('Individual Value')
plt.title('I Chart of Manufacturing Defects')
plt.legend()
plt.show()

# Manage Control Limits: Use only the first 20 values to calculate control limits
first_20_values = manufacturing_defects[:20]
x_bar_20 = np.mean(first_20_values)
moving_range_20 = first_20_values.diff().abs().dropna()
mr_bar_20 = np.mean(moving_range_20)

# Calculate new control limits based on the first 20 values
UCL_20 = x_bar_20 + (mr_bar_20 / D2) * 3
LCL_20 = x_bar_20 - (mr_bar_20 / D2) * 3

# Plot with new control limits including additional data points
plt.figure(figsize=(10, 6))
plt.plot(manufacturing_defects, marker='o', linestyle='-', color='b', label='Individual Values')
plt.axhline(y=x_bar_20, color='green', linestyle='-', linewidth=2, label='Center Line (Mean, first 20)')
plt.axhline(y=UCL_20, color='red', linestyle='--', linewidth=2, label='Upper Control Limit (UCL, first 20)')
plt.axhline(y=LCL_20, color='red', linestyle='--', linewidth=2, label='Lower Control Limit (LCL, first 20)')
plt.text(18, 1000, "These were due to NPI.\nExcluded from control limits\ncalculation", fontsize=8)
plt.xlabel('Observations')
plt.ylabel('Individual Value')
plt.title('I Chart of Manufacturing Defects (First 20 Control Limits)')
plt.legend()
plt.show()

# Generate random data and add specification limits
random_data = np.random.normal(70, 10, 20)
x_bar_random = np.mean(random_data)
mr_random = np.mean(np.abs(np.diff(random_data)))
UCL_random = x_bar_random + (mr_random / D2) * 3
LCL_random = x_bar_random - (mr_random / D2) * 3

plt.figure(figsize=(10, 6))
plt.plot(random_data, marker='o', linestyle='-', color='b', label='Individual Values')
plt.axhline(y=x_bar_random, color='green', linestyle='-', linewidth=2, label='Center Line (Mean)')
plt.axhline(y=UCL_random, color='red', linestyle='--', linewidth=2, label='Upper Control Limit (UCL)')
plt.axhline(y=LCL_random, color='red', linestyle='--', linewidth=2, label='Lower Control Limit (LCL)')
plt.axhline(y=120, color='red', linestyle='-', linewidth=2, label='USL')
plt.text(0, 120, "USL", fontsize=8)
plt.axhline(y=30, color='red', linestyle='-', linewidth=2, label='LSL')
plt.text(0, 30, "LSL", fontsize=8)
plt.xlabel('Observations')
plt.ylabel('Individual Value')
plt.title('I Chart with Specification Limits')
plt.legend()
plt.show()
