# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import os
from statsmodels.graphics.gofplots import qqplot


# Load the data
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')  # Navigate to the data folder
data_file = os.path.join(data_folder, 'EYES.CSV')  # Full path to the CSV file

# Load the dataset
# Use pandas to read the CSV file
# The 'na_values' parameter replaces "NA" strings in the dataset with NaN (missing values)
dataset = pd.read_csv(data_file, na_values="NA")

# Simplified QQ plot without confidence intervals
plt.figure(figsize=(8, 6))
stats.probplot(dataset['One(30)'].dropna(), dist="norm", plot=plt)
plt.title("Normal Q-Q Plot")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.show()

# More advanced QQ plot with 95% confidence interval
# We use the statsmodels library for more advanced plots
plt.figure(figsize=(8, 6))
qqplot(dataset['One(30)'].dropna(), line='s')
plt.title("Probability Plot of First Column in Dataset")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.show()

# Anderson-Darling Test for Normality and adding the result to the plot
from scipy.stats import anderson

# Calculate the statistics
sample_data = dataset['One(30)'].dropna()
mean = np.mean(sample_data)
std_dev = np.std(sample_data)
ad_test_result = anderson(sample_data, dist='norm')
AD_statistic = ad_test_result.statistic

# Plotting the QQ plot and showing statistics on the graph
plt.figure(figsize=(8, 6))
qqplot(sample_data, line='s')
plt.title("Probability Plot with Anderson-Darling Test Result")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.text(-2, max(sample_data) * 0.8, f"Mean: {mean:.2f}\nStDev: {std_dev:.2f}\nAD Statistic: {AD_statistic:.3f}", fontsize=10)
plt.show()

# Load the next dataset
datafile_failures =  os.path.join(data_folder, 'FAILURES.CSV') 
dataset_failures = pd.read_csv(datafile_failures, na_values="NA")
y = dataset_failures['Telford']

# Histogram to visualize the distribution of data
plt.figure(figsize=(8, 6))
plt.hist(y.dropna(), bins=20, edgecolor='black')
plt.title("Histogram of Telford")
plt.xlabel("Failure Rate")
plt.ylabel("Frequency")
plt.show()

# Test for Normality using QQ plot
plt.figure(figsize=(8, 6))
qqplot(y.dropna(), line='s')
plt.title("Probability Plot of Telford")
plt.xlabel("Theoretical Quantiles")
plt.ylabel("Sample Quantiles")
plt.show()

# Time Series plot
plt.figure(figsize=(10, 6))
plt.plot(y.dropna(), marker='o', linestyle='-', color='b')
plt.title("Time Series Plot of Telford")
plt.xlabel("Index")
plt.ylabel("Failure Rate")
plt.show()

# Dotplot
plt.figure(figsize=(8, 6))
plt.plot(y.dropna(), 'o', color='blue')
plt.title("Dotplot of Telford")
plt.xlabel("Index")
plt.ylabel("Failure Rate")
plt.box(on=True)
plt.show()
