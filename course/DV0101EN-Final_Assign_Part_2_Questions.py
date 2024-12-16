#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import more_itertools
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("Automobile Sales Statistics Dashboard", style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    #TASK 2.2: Add two dropdown menus
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            value=None,  # No default value
            placeholder='Select a report type',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value=None,  # No default value
            placeholder='Select a year',
            style={'width': '80%', 'padding': '3px', 'font-size': '20px', 'text-align-last': 'center'}
        )),
    html.Div([  # TASK 2.3: Add a division for output display
    html.Div(id='output-container', 
        style={
            'display': 'grid',
            'grid-template-columns': 'repeat(2, 1fr)',  # Creates 2 equal columns
            'grid-template-rows': 'repeat(2, 1fr)',     # Creates 2 equal rows
            'gap': '20px',                             # Adds spacing between grid items
            'padding': '20px',
            'height': '800px'                          # Fixed height to ensure proper sizing
        }
    )
])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
     Input(component_id='select-year', component_property='value')])
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
        # Plot 1: Automobile sales fluctuation over Recession Period
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales fluctuation over Recession Period")
        )

        # Plot 2: Average vehicles sold by vehicle type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                 
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title="Average Number of Vehicles Sold by Vehicle Type")
        )
        
        # Plot 3: Total expenditure share by vehicle type
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                names='Vehicle_Type',
                values='Advertising_Expenditure',
                title="Total Expenditure Share by Vehicle Type during Recessions")
        )

        # Plot 4: Effect of unemployment rate on vehicle type and sales
        unemp_data = recession_data.groupby(['Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        unemp_data['unemployment_rate'] = recession_data['unemployment_rate'].mean()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_data,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title='Average Automobile Sales by Vehicle Type During Unemployment (Recession)',
                labels={'Automobile_Sales': 'Average Sales'})
        )

        # For both Yearly and Recession statistics, replace the return statements with:
        return [
            html.Div(R_chart1),  # or R_chart1
            html.Div(R_chart2),  # or R_chart2
            html.Div(R_chart3),  # or R_chart3
            html.Div(R_chart4)   # or R_chart4
        ]

    elif selected_statistics == 'Yearly Statistics' and input_year:
        yearly_data = data[data['Year'] == input_year]
        
        # Plot 1: Yearly Automobile sales
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas,
                x='Year',
                y='Automobile_Sales',
                title="Yearly Automobile Sales")
        )
            
        # Plot 2: Monthly Automobile sales for selected year
        mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(mas,
                x='Month',
                y='Automobile_Sales',
                title=f'Monthly Automobile Sales for {input_year}')
        )

        # Plot 3: Average vehicles sold by type
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata,
                x='Vehicle_Type',
                y='Automobile_Sales',
                title=f'Average Vehicles Sold by Vehicle Type in {input_year}')
        )

        # Plot 4: Total Advertisement Expenditure by vehicle type
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data,
                values='Advertising_Expenditure',
                names='Vehicle_Type',
                title='Total Advertisement Expenditure by Vehicle Type')
        )

        return [
            html.Div(Y_chart1),  # or R_chart1
            html.Div(Y_chart2),  # or R_chart2
            html.Div(Y_chart3),  # or R_chart3
            html.Div(Y_chart4)   # or R_chart4
        ]
        
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)


# %%
