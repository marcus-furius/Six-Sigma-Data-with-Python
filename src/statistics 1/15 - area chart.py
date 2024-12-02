import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 1: Create and save example CSV data
# We will create a DataFrame with expanded data representing the lead time (in days) to create various deliverables

data = {
    'Requirement Analysis': [10, 15, 10, 12, 14, 13],
    'Design Specification': [20, 25, 22, 24, 26, 23],
    'Development': [30, 35, 31, 33, 32, 34],
    'Testing': [15, 18, 14, 16, 15, 17],
    'Deployment': [5, 5, 6, 5, 7, 5],
    'User Training': [8, 10, 7, 9, 8, 10],
    'Documentation': [12, 12, 11, 13, 12, 12]
}

# Create a DataFrame
df = pd.DataFrame(data, index=['Project A', 'Project B', 'Project C', 'Project D', 'Project E', 'Project F'])

# Save the DataFrame to a CSV file
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'lead_time_data.CSV')
df.to_csv(data_file, index=True)

# Step 2: Read the CSV file
df = pd.read_csv(data_file, index_col=0)

# Generating an area chart to visualize cumulative lead times of different deliverables across projects

# Plotting the area chart
plt.figure(figsize=(12, 8))
df.plot(kind='area', stacked=True, alpha=0.4, figsize=(14, 8))
plt.title('Cumulative Lead Times for Various Deliverables Across Projects')
plt.xlabel('Projects')
plt.ylabel('Cumulative Lead Time (days)')
plt.legend(title='Deliverables', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()