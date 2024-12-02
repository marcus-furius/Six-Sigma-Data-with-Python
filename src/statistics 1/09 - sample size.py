# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate sample size for estimating averages (continuous data)
# d: desired precision
# s: standard deviation
# This function returns the required sample size to estimate an average to within a specified precision.
def sample_size_continuous(d, s):
    # Using the formula for sample size estimation: ((2 * s) / d) ** 2
    # 2 * s is used to approximate the 95% confidence interval
    result = ((2 * s) / d) ** 2
    return result

# Example 1: Estimating average length of incoming calls
# Desired precision is 1 minute (d=1)
# Historical standard deviation is 3 minutes (s=3)
d = 1
s = 3
sample_size = sample_size_continuous(d, s)
print(f"Sample Size for continuous data with precision {d} and standard deviation {s}: {sample_size}")

# Function to create a sample size table for a range of precisions
# s: standard deviation
def sample_size_continuous_table(s):
    # Start precision at 1% of the standard deviation
    precision_start = s / 100
    precisions = [precision_start * (i + 1) for i in range(100)]  # Create a list of 100 precision values
    sizes = [sample_size_continuous(precision, s) for precision in precisions]  # Calculate sample size for each precision
    
    # Create a DataFrame with precision and sample size
    df = pd.DataFrame({
        'Precision': precisions,
        'Sample Size': sizes
    })
    return df

# Create sample size table for a standard deviation of 3
sample_size_table = sample_size_continuous_table(3)

# Plot the first 20 rows of the sample size table
plt.figure(figsize=(10, 6))
plt.plot(sample_size_table['Precision'][:20], sample_size_table['Sample Size'][:20], marker='o')
plt.title('Precision vs Sample Size (95% CI)')
plt.xlabel('Precision')
plt.ylabel('Sample Size')
plt.grid(True)
plt.show()

# Function to calculate sample size for estimating proportions (discrete data)
# d: desired precision (as a decimal)
# p: estimated proportion (as a decimal)
# This function returns the required sample size to estimate a proportion to within a specified precision.
def sample_size_discrete(d, p):
    # Using the formula for sample size estimation for proportions: (((2) / d) ** 2) * p * (1 - p)
    result = (((2) / d) ** 2) * p * (1 - p)
    return result

# Example 2: Estimating proportion of defective products
# Estimated proportion defective is 10% (p=0.10)
# Desired precision is 3% (d=0.03)
d = 0.03
p = 0.10
sample_size = sample_size_discrete(d, p)
print(f"Sample Size for discrete data with precision {d} and proportion {p}: {sample_size}")

# Estimating proportion with a precision of 1% (d=0.01)
d = 0.01
sample_size = sample_size_discrete(d, p)
print(f"Sample Size for discrete data with precision {d} and proportion {p}: {sample_size}")

# Function to create a sample size table for discrete data
# p: estimated proportion
def sample_size_discrete_table(p):
    # Start precision at 1/10th of the proportion
    precision_start = p / 10
    precisions = [precision_start * (i + 1) for i in range(100)]  # Create a list of 100 precision values
    sizes = [sample_size_discrete(precision, p) for precision in precisions]  # Calculate sample size for each precision
    
    # Create a DataFrame with precision and sample size
    df = pd.DataFrame({
        'Precision': precisions,
        'Sample Size': sizes
    })
    return df

# Create sample size table for a proportion of 0.01
sample_size_table_discrete = sample_size_discrete_table(0.01)

# Plot the first 20 rows of the sample size table for discrete data
plt.figure(figsize=(10, 6))
plt.plot(sample_size_table_discrete['Precision'][:20], sample_size_table_discrete['Sample Size'][:20], marker='o')
plt.title('Precision vs Sample Size (95% CI)')
plt.xlabel('Precision')
plt.ylabel('Sample Size')
plt.grid(True)
plt.show()
