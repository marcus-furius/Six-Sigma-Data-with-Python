""" 
import pandas as pd
import matplotlib.pyplot as plt

# Load the JSON file
file_path = 'C:\\Users\\marcu\\OneDrive\\Documents\\Downloads\\jobs.json'  # Replace with the path to your JSON file
df = pd.read_json(file_path)

# Count the number of job postings by location (or use a different column if needed)
job_postings_count = df['Location'].value_counts()

# Plot a bar chart in descending order
plt.figure(figsize=(12, 6))
job_postings_count.plot(kind='bar', color='skyblue')
plt.title('Job Postings by Location')
plt.xlabel('Location')
plt.ylabel('Number of Job Postings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() """


import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data = {
    "Language": ["Python", "Java", "R", "Javascript", "Swift", "C++", "C#", "PHP", "SQL", "Go"],
    "Average Annual Salary": [114383, 101013, 92037, 110981, 130801, 113865, 88726, 84727, 84793, 94082]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the data in descending order of Average Annual Salary
df_sorted = df.sort_values(by="Average Annual Salary", ascending=False)

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df_sorted["Language"], df_sorted["Average Annual Salary"], color='skyblue')
plt.title("Average Annual Salary by Programming Language")
plt.xlabel("Programming Language")
plt.ylabel("Average Annual Salary (USD)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
