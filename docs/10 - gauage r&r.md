### Gage R&R Study in Python: A Comprehensive Guide

#### 1. Purpose and Use Cases
**Gage R&R Analysis** is a method used to quantify the variation in measurement systems, particularly when multiple operators are involved in measuring parts. This is crucial in manufacturing and quality control to determine if the measuring process is reliable.

**When to Use Gage R&R Analysis:**
- To evaluate measurement consistency across operators and parts.
- To assess whether observed variability is due to actual product differences or issues in the measurement system.

**Data Requirements:**
1. **Operators**: Different individuals performing measurements.
2. **Parts**: Different units being measured.
3. **Measurements**: Repeated readings by operators on parts.

#### 2. Code Structure and Implementation

##### Step 1: Experimental Design
```python
import pandas as pd
import numpy as np

# Set the number of operators, parts, and measurements
operators = 3
parts = 10
measurements = 3

# Create the experimental design dataframe
np.random.seed(42)  # for reproducibility
design = {
    'Operator': np.repeat(np.arange(1, operators + 1), parts * measurements),
    'Part': np.tile(np.repeat(np.arange(1, parts + 1), measurements), operators),
    'Measurement': np.nan  # placeholder for actual measurement values
}
design_df = pd.DataFrame(design)

# Export the experimental design to CSV for data entry
datafile = "GRR_JTS.csv"
design_df.to_csv(datafile, index=False)
print(f"Experimental design saved to {datafile} for data capture.")
```
**Purpose:**
- Set up a study with a specified number of operators, parts, and measurements.
- Create a CSV to record actual measurement data.

##### Step 2: Data Loading
```python
import os

data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'GRR JTS COMPLETE.csv')
dataset = pd.read_csv(data_file)

# Extract measurement data from the dataset
design_df['Measurement'] = dataset['Measurement']
```
**Purpose:**
- Load completed measurement data into the experimental design dataframe.

##### Step 3: Gage R&R Analysis
```python
# Calculate the mean for each part/operator combination
part_operator_mean = design_df.groupby(['Part', 'Operator'])['Measurement'].mean().unstack()
part_mean = design_df.groupby('Part')['Measurement'].mean()
operator_mean = design_df.groupby('Operator')['Measurement'].mean()
total_mean = design_df['Measurement'].mean()

# Calculate Repeatability and Reproducibility
repeatability = design_df.groupby(['Part', 'Operator'])['Measurement'].std().mean()  # Within part/operator variation
reproducibility = operator_mean.std()  # Variation between operators
part_to_part_variation = part_mean.std()  # Variation between parts

# Calculate Total Gage R&R
total_gage_rr = np.sqrt(repeatability**2 + reproducibility**2)
total_variation = np.sqrt(repeatability**2 + reproducibility**2 + part_to_part_variation**2)

# Contribution percentages
repeatability_percent = (repeatability**2 / total_variation**2) * 100
reproducibility_percent = (reproducibility**2 / total_variation**2) * 100
part_to_part_percent = (part_to_part_variation**2 / total_variation**2) * 100
total_gage_rr_percent = (total_gage_rr**2 / total_variation**2) * 100

# Output summary
print("Gage R&R Analysis Summary:")
print(f"Overall Mean: {total_mean:.2f}")
print(f"Repeatability: {repeatability:.2f}")
print(f"Reproducibility: {reproducibility:.2f}")
print(f"Part-to-Part Variation: {part_to_part_variation:.2f}")
print(f"Total Gage R&R: {total_gage_rr:.2f}")
print(f"Total Variation: {total_variation:.2f}")
print("\n% Contribution:")
print(f"Repeatability: {repeatability_percent:.2f}%")
print(f"Reproducibility: {reproducibility_percent:.2f}%")
print(f"Part-to-Part: {part_to_part_percent:.2f}%")
print(f"Total Gage R&R: {total_gage_rr_percent:.2f}%")
```
**Analysis Provided:**
- Calculated **Repeatability**, **Reproducibility**, **Part-to-Part Variation**, and **Total Gage R&R**.
- Quantified the contributions of each component to total variation.

##### Step 4: Flagging Measurement System Quality
```python
# Flagging the result of the study
if total_gage_rr_percent < 10:
    flag_message = "The measurement system is considered acceptable and very precise."
elif 10 <= total_gage_rr_percent <= 30:
    flag_message = "The measurement system is acceptable depending on other factors, such as cost or importance."
else:
    flag_message = "The measurement system is unacceptable and needs improvement."
print(f"\nResult Flag: {flag_message}")
```
**Criteria:**
- Less than **10%**: Acceptable and precise.
- Between **10% and 30%**: Conditionally acceptable.
- Greater than **30%**: Unacceptable; needs improvement.

##### Step 5: Visualization
```python
import matplotlib.pyplot as plt

# Plot measurement variation by operator
plt.figure(figsize=(10, 6))
plt.boxplot([design_df[design_df['Operator'] == i]['Measurement'] for i in design_df['Operator'].unique()],
            labels=[f'Operator {i}' for i in design_df['Operator'].unique()])
plt.title('Measurement Variation by Operator')
plt.xlabel('Operator')
plt.ylabel('Measurement')
plt.show()

# Plot contribution to total variation
plt.figure(figsize=(10, 6))
contributions = [repeatability_percent, reproducibility_percent, part_to_part_percent, total_gage_rr_percent]
labels = ['Repeatability', 'Reproducibility', 'Part-to-Part', 'Total Gage R&R']
plt.bar(labels, contributions, color='skyblue')
plt.title('% Contribution to Total Variation')
plt.xlabel('Source of Variation')
plt.ylabel('% Contribution')
plt.ylim(0, 100)
plt.show()
```
**Purpose:**
- Box plot to visualize **variation by operator**.
- Bar chart to illustrate **% contribution** of each factor to total variation.

#### 3. Summary and Insights
- **Repeatability** indicates the consistency of measurements taken by the same operator.
- **Reproducibility** assesses differences across operators.
- **Part-to-Part** variation shows differences between the actual parts.
- A high **Total Gage R&R** suggests significant issues in the measurement process that must be addressed for reliable quality control.

#### 4. Practical Considerations
- **Data Integrity**: Ensure measurements are accurate and recorded consistently.
- **Further Analysis**: If **Total Gage R&R** exceeds 30%, consider evaluating the measurement tools or retraining operators.

#### 5. Applications
- **Manufacturing**: To validate measurement systems used for quality checks.
- **Quality Control**: Helps in understanding and improving process consistency.
- **Research & Development**: Ensures data accuracy during experimental trials.

