# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: Create a normal distribution with a mean of 50, a standard deviation of 5, and a sample size of 1000
# Using numpy's random.normal to generate random data with a normal distribution
np.random.seed(42)  # Setting a seed for reproducibility
mean = 50
std_dev = 5
sample_size = 1000
normal_data = np.random.normal(mean, std_dev, sample_size)

# Step 2: Plot a histogram of the data
plt.hist(normal_data, bins=30, density=True, alpha=0.6, color='g')

# Step 3: Add the normal curve to the histogram
# The norm.pdf function from scipy.stats calculates the height of the normal curve for given points
xmin, xmax = plt.xlim()  # Get the range for x-axis
x = np.linspace(xmin, xmax, 100)  # Create points across the x range
y = norm.pdf(x, mean, std_dev)  # Calculate normal distribution values for the points
plt.plot(x, y, color='darkblue', linewidth=2)

# Step 4: Add probability lines at the mean and at 1, 2, and 3 standard deviations from the mean
# This helps visualize the spread and normal distribution properties
for i in range(-3, 4):
    label = f"{i:+d}s" if i != 0 else "xbar"
    plt.axvline(mean + i * std_dev, color='red', linestyle='--', linewidth=1)
    plt.text(mean + i * std_dev, 0.01, label, color='black', fontsize=8, ha='center')

# Display the histogram and normal curve
plt.title('Normal Distribution (Mean = 50, SD = 5)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

# Step 5: Calculate the percentage of values above the upper specification limit (USL)
# Given: Mean (xbar) = 14.203, Standard Deviation (S) = 0.0829, Upper Specification Limit (USL) = 14.4
xbar = 14.203
S = 0.0829
USL = 14.4

# Use norm.sf (survival function) to calculate the probability of values greater than the USL
# Alternatively, you can use 1 - norm.cdf() to achieve the same result
p = norm.sf(USL, loc=xbar, scale=S)

# Convert the probability to percentage
result_percentage = p * 100
print(f"Percentage of day's output predicted to be above the USL: {result_percentage:.2f}%")