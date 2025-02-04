import plotly.graph_objects as go

# Parameters
x = [
    '2024 Actual', 'Inflation', '2024 Support: Digital', '2024 Support: Other',
    '2024 Hardware Refresh', '2025 Baseline', 'Additional Staff',
    'New Ticketing System', 'DC Consolidation', 'XYZ Renegotiation',
    'Staff Savings', 'Other Savings', 'Total 2025'
]
y = [90.3, -3.3, -5.4, -4.7, -1.3, 102.4, -1.4, -1.0, 2.5, 3.1, 1.3, 4.3, 93.6]

# measures
measure=["total", "relative", "relative", "relative", "relative", "total", "relative", "relative", "relative", "relative","relative", "relative","total"]

# Add labels for the values
text = [f"{value:+.1f}" for value in y[:-1]] + ["Total"]

# Create the Waterfall chart
fig = go.Figure(go.Waterfall(
    name="2024-2025 Movement",
    orientation="v",
    measure=measure,
    x=x,
    y=y,
    textposition="outside",
    text=text,
    connector={"line": {"color": "rgb(63, 63, 63)"}},
    decreasing={"marker": {"color": "red"}},
    increasing={"marker": {"color": "green"}},
    totals={"marker": {"color": "blue"}}
))

# Update layout
fig.update_layout(
    title="IT Operations — Movement From 2024 to 2025 ($m)",
    showlegend=False,
    xaxis_title="Categories",
    yaxis_title="Value ($m)",
    waterfallgap=0.3
)

# Show the figure
fig.show()
