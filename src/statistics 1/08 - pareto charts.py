import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def create_pareto(data, title="Pareto Chart", figsize=(10, 6)):
    """
    Creates a Pareto chart from frequency data
    
    Parameters:
    data (pd.Series): Series containing frequency counts
    title (str): Title for the chart
    figsize (tuple): Figure dimensions
    
    Returns:
    tuple: Frequency counts and cumulative percentages
    """
    # Sort data in descending order
    sorted_data = data.sort_values(ascending=False)
    
    # Calculate cumulative percentages
    total = sorted_data.sum()
    cumulative_percent = np.cumsum(sorted_data) / total * 100
    
    # Create figure with two y-axes
    fig, ax1 = plt.subplots(figsize=figsize)
    ax2 = ax1.twinx()
    
    # Plot bars on first y-axis
    bars = ax1.bar(range(len(sorted_data)), sorted_data, color='lightcoral')
    ax1.set_ylabel('Frequency')
    
    # Plot cumulative line on second y-axis
    ax2.plot(range(len(sorted_data)), cumulative_percent, color='navy', 
             marker='o', linewidth=2)
    ax2.set_ylabel('Cumulative Percentage')
    
    # Set the tick labels
    plt.xticks(range(len(sorted_data)), sorted_data.index, rotation=45, ha='right')
    
    # Set y-axis ranges
    ax2.set_ylim([0, 105])  # Goes to 105% to prevent line being cut off
    
    # Add gridlines
    ax1.yaxis.grid(True)
    
    plt.title(title)
    plt.tight_layout()
    
    return sorted_data, cumulative_percent

# Load the data
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')  # Navigate to the data folder
data_file = os.path.join(data_folder, 'DEFECT TYPES.CSV')  # Full path to the CSV file
defect_data = pd.read_csv(data_file)

# Method 1: Using pre-summarized data
# Extract the defect frequencies from the summary data
defect_freq = pd.Series(data=defect_data['Occurrences'].iloc[:10].values,
                       index=defect_data['Defect'].iloc[:10].values)

# Create first Pareto chart
freq_sorted, cum_percent = create_pareto(defect_freq, 
                                       title="Pareto Chart of Defect Types (Pre-summarized)")
plt.show()

# Method 2: Using raw data
# Create frequency table from coded defects
freq_table = defect_data['Coded Defects'].value_counts()
freq_sorted, cum_percent = create_pareto(freq_table, 
                                       title="Pareto Chart of Defect Types (Raw Data)")
plt.show()

# Analysis by Shifts
# Create a figure with subplots for each shift
shifts = defect_data['Shift'].unique()
fig, axes = plt.subplots(1, len(shifts), figsize=(15, 5))
fig.suptitle('Pareto Charts by Shift')

for i, shift in enumerate(shifts):
    # Filter data for current shift
    shift_data = defect_data[defect_data['Shift'] == shift]
    freq_table = shift_data['Coded Defects'].value_counts()
    
    # Create Pareto chart in current subplot
    if len(shifts) > 1:
        current_ax = axes[i]
    else:
        current_ax = axes
        
    # Create bars
    sorted_data = freq_table.sort_values(ascending=False)
    cumulative_percent = np.cumsum(sorted_data) / sorted_data.sum() * 100
    
    # Create twin axes for frequency and percentage
    ax2 = current_ax.twinx()
    
    # Plot data
    current_ax.bar(range(len(sorted_data)), sorted_data, color='lightcoral')
    ax2.plot(range(len(sorted_data)), cumulative_percent, color='navy', 
             marker='o', linewidth=2)
    
    # Customize axes
    current_ax.set_title(shift)
    if i == 0:
        current_ax.set_ylabel('Frequency')
    if i == len(shifts) - 1:
        ax2.set_ylabel('Cumulative %')
    
    # Set tick labels
    current_ax.set_xticks(range(len(sorted_data)))
    current_ax.set_xticklabels(sorted_data.index, rotation=45, ha='right')
    ax2.set_ylim([0, 105])

plt.tight_layout()
plt.show()

# Create descriptive labels Pareto
# Create defect type mapping
defect_mapping = {
    1: "Double Edges",
    2: "Excess Material",
    3: "Nicks",
    4: "Rough Edges",
    5: "Splits",
    6: "Stress Tears",
    7: "Tears",
    8: "Unfilled",
    9: "Wisps",
    10: "Unknown"
}

# Map coded defects to descriptive labels
defect_data['Defect_Type'] = defect_data['Coded Defects'].map(defect_mapping)

# Create frequency table with descriptive labels
freq_table = defect_data['Defect_Type'].value_counts()

# Create final Pareto chart with descriptive labels
freq_sorted, cum_percent = create_pareto(freq_table, 
                                       title="Pareto Chart of Defect Types (Descriptive Labels)")
plt.show()