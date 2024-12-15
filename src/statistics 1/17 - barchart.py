# Import necessary libraries
import matplotlib.pyplot as plt

# Step 1: Define the data
# Data for the bar chart (example: top 10 countries by population in 2023)
countries = [
    "China", "India", "USA", "Indonesia", "Pakistan", 
    "Nigeria", "Brazil", "Bangladesh", "Russia", "Mexico"
]
populations = [
    1425890000, 1416413000, 335903000, 280345000, 241450000,
    223804632, 216410865, 173834762, 146170000, 132582000
]

# Step 2: Convert population to billions for better readability
populations_in_billions = [pop / 1e9 for pop in populations]

# Step 3: Create the bar chart
plt.figure(figsize=(12, 8))  # Set the figure size
plt.bar(countries, populations_in_billions, color='skyblue', alpha=0.8)

# Step 4: Add titles and labels
plt.title("Top 10 Countries by Population (2023)", fontsize=16)
plt.xlabel("Countries", fontsize=14)
plt.ylabel("Population (Billions)", fontsize=14)

# Step 5: Customize the axes
plt.xticks(rotation=45, fontsize=12)  # Rotate country labels for better readability
plt.yticks(fontsize=12)

# Step 6: Display the plot
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
