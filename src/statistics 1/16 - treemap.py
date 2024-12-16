# Import necessary libraries
import squarify  # Library for creating treemaps [py -m pip install squarify]
import matplotlib.pyplot as plt

# Step 1: Define the data
# Data for the treemap (example: top 10 countries by population in 2023)
countries = [
    "China", "India", "USA", "Indonesia", "Pakistan", 
    "Nigeria", "Brazil", "Bangladesh", "Russia", "Mexico"
]
populations = [
    1425890000, 1416413000, 335903000, 280345000, 241450000,
    223804632, 216410865, 173834762, 146170000, 132582000
]

# Step 2: Normalize the data for treemap
# Squarify requires values to be normalized to fit into the plotting area
# The squarify.normalize_sizes function adjusts the sizes for plotting
normalized_populations = squarify.normalize_sizes(populations, 100, 100)

# Step 3: Create the treemap
# Use squarify.plot to generate the treemap
plt.figure(figsize=(12, 8))  # Set the size of the figure
squarify.plot(
    sizes=normalized_populations,  # The data values for the treemap
    label=countries,               # Labels for the treemap rectangles
    color=plt.cm.Paired.colors,    # Add colors from a colormap
    alpha=0.8                      # Transparency of the colors
)

# Step 4: Customize the plot
# Remove axes for a cleaner look
plt.axis('off')  
# Add a title to the treemap
plt.title("Top 10 Countries by Population (2023)", fontsize=16)

# Step 5: Display the plot
plt.show()


# ADVANCED VERSION

import plotly.express as px
import pandas as pd

# Create sample data for tech companies market cap (in billions USD)
# This is simplified public data from major tech companies
data = {
    'Company': ['Apple', 'Microsoft', 'Alphabet', 'Amazon', 'Meta',
                'NVIDIA', 'Tesla', 'Samsung', 'TSMC', 'Tencent'],
    'Market_Cap': [3000, 2800, 1900, 1700, 1200,
                   1100, 800, 600, 500, 400],
    'Sector': ['Consumer Electronics', 'Software', 'Internet Services', 'E-commerce', 'Social Media',
               'Semiconductors', 'Automotive', 'Electronics', 'Semiconductors', 'Internet Services']
}

# Convert the dictionary to a pandas DataFrame
# DataFrame is a 2-dimensional labeled data structure
df = pd.DataFrame(data)

# Create the treemap using plotly express
# Parameters explained:
# - data_frame: our DataFrame containing the data
# - path: defines the hierarchy of the treemap (companies nested within sectors)
# - values: the size of each rectangle (market cap)
# - title: title of the visualization
# - color: color the rectangles based on market cap
# - color_continuous_scale: choose a color palette (blue to green)
treemap = px.treemap(
    data_frame=df,
    path=[px.Constant("All Companies"), 'Sector', 'Company'],  # Hierarchy levels
    values='Market_Cap',
    title='Tech Companies Market Capitalization Treemap',
    color='Market_Cap',
    color_continuous_scale='blues',
    hover_data=['Market_Cap']
)

# Update the layout for better visibility
treemap.update_traces(
    textinfo="label+value",  # Show both label and value
    hovertemplate='<b>%{label}</b><br>Market Cap: $%{value}B<extra></extra>'  # Custom hover text
)

# Update layout settings
treemap.update_layout(
    width=1000,  # Width of the plot
    height=600,  # Height of the plot
    title_x=0.5,  # Center the title
    title_font_size=20  # Increase title font size
)

# Display the treemap
treemap.show()