import pandas as pd
import plotly.graph_objects as go
import re
from pathlib import Path

# Load the Excel file
scorecard_data = pd.read_excel(
    "C:/Users/dharris/OneDrive - Jazzpharma.com/Project/Jazz.ISStrategy/scorecard-data (1).xlsx",
    sheet_name="scorecard-data 2024"
)

# Status indicator mapping
STATUS_INDICATORS = {
    'G': '🟢',
    'Y': '🟡',
    'R': '🔴',
    'B': '🔵'
}

def create_status_indicator(status):
    """Convert status letters to corresponding emoji indicators"""
    if pd.isna(status):
        return status
    return ''.join(STATUS_INDICATORS.get(char, char) for char in str(status))

# Data preprocessing
def preprocess_data(df):
    # Convert YTD/Quarter Result to numeric, removing % and dividing by 100
    df = df.copy()
    df['YTD or Quarter Result'] = df['YTD or Quarter Result'].str.rstrip('%').astype(float) / 100
    
    # Apply status indicators
    df['Status'] = df['Status'].apply(create_status_indicator)
    
    return df

# Create color conditions for trend arrows
def get_trend_color(value):
    if pd.isna(value):
        return 'black'
    if '▲' in str(value):
        return 'darkgreen'
    if '▼' in str(value):
        return 'darkred'
    return 'black'

# Process the data
processed_data = preprocess_data(scorecard_data)

# Create the table using plotly
fig = go.Figure(data=[go.Table(
    header=dict(
        values=list(processed_data.columns),
        fill_color='#E8E8E8',
        align=['left'] * len(processed_data.columns),
        font=dict(size=11, weight='bold')
    ),
    cells=dict(
        values=[processed_data[col] for col in processed_data.columns],
        align=['left'] * (len(processed_data.columns) - 1) + ['right'],
        font=dict(size=11),
        format=[
            None,  # Strategy Category
            None,  # Principle, Maxim or Strategic Statement
            None,  # KPI or Metric Name
            None,  # Update Period
            None,  # Status
            None,  # Target
            '.1%',  # YTD or Quarter Result
            None   # Moving Annual Average & Trend
        ],
        height=30
    )
)])

# Update layout
fig.update_layout(
    title=dict(
        text='IS Strategy, Operations, and Compliance Scorecard – December 2024',
        x=0,
        font=dict(size=14, weight='bold')
    ),
    width=1200,
    height=len(processed_data) * 35 + 100,
    margin=dict(t=50, b=20, l=20, r=20)
)

# Set column widths
fig.update_layout(
    columnwidth=[120, 250, 200, 100, 80, 80, 100, 120]
)

# Display the table
fig.show()

# Optionally, save to HTML
fig.write_html("scorecard_table.html")