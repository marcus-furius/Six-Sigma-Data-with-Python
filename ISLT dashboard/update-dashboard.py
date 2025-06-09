#!/usr/bin/env python
import csv
import os
from datetime import datetime
import pandas as pd
from bs4 import BeautifulSoup

def load_dashboard_data(csv_path):
    """Load data from CSV file into DataFrame"""
    df = pd.read_csv(csv_path)
    return df

def calculate_summary_metrics(df):
    """Calculate summary metrics for the dashboard"""
    total_objectives = len(df)
    overall_completion = round(df['progress'].mean())
    
    on_track = len(df[df['status'] == 'Green'])
    at_risk = len(df[df['status'] == 'Amber'])
    critical = len(df[df['status'] == 'Red'])
    
    return {
        'total_objectives': total_objectives,
        'overall_completion': overall_completion,
        'on_track': on_track,
        'at_risk': at_risk,
        'critical': critical
    }

def calculate_pillar_metrics(df):
    """Calculate metrics for each pillar"""
    pillar_metrics = {}
    
    for pillar in df['pillar'].unique():
        pillar_df = df[df['pillar'] == pillar]
        pillar_progress = round(pillar_df['progress'].mean())
        
        # Determine overall pillar status based on objective statuses
        if 'Red' in pillar_df['status'].values:
            pillar_status = 'Red'
        elif 'Amber' in pillar_df['status'].values:
            pillar_status = 'Amber'
        else:
            pillar_status = 'Green'
            
        pillar_metrics[pillar] = {
            'progress': pillar_progress,
            'status': pillar_status,
            'objectives': pillar_df.to_dict('records')
        }
    
    return pillar_metrics

def update_html_dashboard(template_path, output_path, df):
    """Update the HTML dashboard with new data"""
    with open(template_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Update summary metrics
    summary_metrics = calculate_summary_metrics(df)
    
    # Update overall completion
    completion_value = soup.select_one('.summary-tile .value')
    if completion_value:
        completion_value.string = f"{summary_metrics['overall_completion']}%"
    
    completion_bar = soup.select_one('.summary-tile .progress-bar')
    if completion_bar:
        completion_bar['style'] = f"width: {summary_metrics['overall_completion']}%; background-color: var(--blue);"
    
    # Update on track objectives
    on_track_value = soup.select('.summary-tile .value')[1]
    if on_track_value:
        on_track_value.string = str(summary_metrics['on_track'])
    
    # Update at risk objectives
    at_risk_value = soup.select('.summary-tile .value')[2]
    if at_risk_value:
        at_risk_value.string = str(summary_metrics['at_risk'])
    
    # Update critical objectives
    critical_value = soup.select('.summary-tile .value')[3]
    if critical_value:
        critical_value.string = str(summary_metrics['critical'])
    
    # Update pillar metrics
    pillar_metrics = calculate_pillar_metrics(df)
    pillar_cards = soup.select('.pillar-card')
    
    pillar_mapping = {
        'Digital Experience': 0,
        'Enterprise Data Analytics/AI': 1,
        'Operations': 2,
        'Culture': 3
    }
    
    for pillar, index in pillar_mapping.items():
        if index < len(pillar_cards) and pillar in pillar_metrics:
            pillar_data = pillar_metrics[pillar]
            card = pillar_cards[index]
            
            # Update progress
            progress_bar = card.select_one('.pillar-progress-bar')
            if progress_bar:
                color = get_color_for_pillar(pillar)
                progress_bar['style'] = f"width: {pillar_data['progress']}%; background-color: {color};"
            
            progress_text = card.select_one('.pillar-progress div:nth-child(3)')
            if progress_text:
                progress_text.string = f"{pillar_data['progress']}%"
            
            # Update status
            status_indicator = card.select_one('.status-indicator')
            if status_indicator:
                update_status_indicator(status_indicator, pillar_data['status'])
            
            # Update objectives table
            objectives_table = card.select_one('.objectives-table tbody')
            if objectives_table:
                update_objectives_table(objectives_table, pillar_data['objectives'])
    
    # Update detailed view table
    detailed_table = soup.select_one('.detailed-view .objectives-table tbody')
    if detailed_table:
        update_detailed_table(detailed_table, df)
    
    # Update last updated timestamp
    last_updated = soup.select_one('.last-updated')
    if last_updated:
        last_updated.string = f"Last updated: {datetime.now().strftime('%B %d, %Y')}"
    
    # Save updated HTML
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))
    
    print(f"Dashboard updated successfully and saved to {output_path}")

def update_objectives_table(table, objectives):
    """Update the objectives table for a pillar"""
    # Clear existing rows
    table.clear()
    
    # Add new rows
    for obj in objectives:
        row = BeautifulSoup().new_tag('tr')
        
        # Objective name cell
        obj_cell = BeautifulSoup().new_tag('td')
        obj_cell.string = obj['objective']
        row.append(obj_cell)
        
        # Quarter status cells
        for quarter in ['q1_status', 'q2_status', 'q3_status', 'q4_status']:
            cell = BeautifulSoup().new_tag('td')
            if obj[quarter]:
                span = BeautifulSoup().new_tag('span', attrs={'class': f"quarter-status {obj[quarter]}"})
                cell.append(span)
            row.append(cell)
        
        table.append(row)

def update_detailed_table(table, df):
    """Update the detailed view table"""
    # Clear existing rows
    table.clear()
    
    # Filter for critical and at-risk items first, then add some on-track
    critical = df[df['status'] == 'Red'].sort_values('progress')
    at_risk = df[df['status'] == 'Amber'].sort_values('progress')
    on_track = df[df['status'] == 'Green'].sort_values('progress', ascending=False).head(3)
    
    # Combine and limit to maximum 10 items
    combined = pd.concat([critical, at_risk, on_track]).head(10)
    
    # Add rows to table
    for _, obj in combined.iterrows():
        row = BeautifulSoup().new_tag('tr')
        
        # Pillar cell
        pillar_cell = BeautifulSoup().new_tag('td')
        pillar_cell.string = obj['pillar']
        row.append(pillar_cell)
        
        # Objective cell
        obj_cell = BeautifulSoup().new_tag('td')
        obj_cell.string = obj['objective']
        row.append(obj_cell)
        
        # Progress cell
        progress_cell = BeautifulSoup().new_tag('td')
        progress_container = BeautifulSoup().new_tag('div', attrs={'class': 'progress-container', 'style': 'margin: 0;'})
        status_color = 'var(--red)' if obj['status'] == 'Red' else 'var(--amber)' if obj['status'] == 'Amber' else 'var(--green)'
        progress_bar = BeautifulSoup().new_tag('div', attrs={
            'class': 'progress-bar',
            'style': f"width: {obj['progress']}%; background-color: {status_color};"
        })
        progress_container.append(progress_bar)
        progress_cell.append(progress_container)
        row.append(progress_cell)
        
        # Status cell
        status_cell = BeautifulSoup().new_tag('td')
        status_indicator = BeautifulSoup().new_tag('div', attrs={'class': f"status-indicator {obj['status'].lower()}"})
        status_text = 'CRITICAL' if obj['status'] == 'Red' else 'AT RISK' if obj['status'] == 'Amber' else 'ON TRACK'
        status_indicator.string = status_text
        status_cell.append(status_indicator)
        row.append(status_cell)
        
        # Owner cell
        owner_cell = BeautifulSoup().new_tag('td')
        owner_cell.string = obj['owner']
        row.append(owner_cell)
        
        # Last update cell
        update_cell = BeautifulSoup().new_tag('td')
        last_update = datetime.strptime(obj['last_update'], '%Y-%m-%d').strftime('%b %d, %Y')
        update_cell.string = last_update
        row.append(update_cell)
        
        table.append(row)

def update_status_indicator(indicator, status):
    """Update the status indicator with the appropriate class and text"""
    # Remove existing status classes
    indicator['class'] = [c for c in indicator.get('class', []) if c not in ['red', 'amber', 'green']]
    
    # Add new status class
    indicator['class'].append(status.lower())
    
    # Update text
    if status == 'Red':
        indicator.string = 'CRITICAL'
    elif status == 'Amber':
        indicator.string = 'AT RISK'
    else:
        indicator.string = 'ON TRACK'

def get_color_for_pillar(pillar):
    """Return the appropriate color variable for a pillar"""
    if pillar == 'Digital Experience':
        return 'var(--dark-blue)'
    elif pillar == 'Enterprise Data Analytics/AI':
        return 'var(--purple)'
    elif pillar == 'Operations':
        return 'var(--blue)'
    elif pillar == 'Culture':
        return 'var(--orange)'
    return 'var(--blue)'  # Default fallback

def main():
    # File paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'dashboard-data.csv')
    template_path = os.path.join(current_dir, 'dashboard-template.html')
    output_path = os.path.join(current_dir, 'is_dashboard.html')
    
    # Check if files exist
    if not os.path.exists(csv_path):
        print(f"Error: CSV file not found at {csv_path}")
        return
    
    if not os.path.exists(template_path):
        print(f"Error: HTML template not found at {template_path}")
        return
    
    # Load data and update dashboard
    df = load_dashboard_data(csv_path)
    update_html_dashboard(template_path, output_path, df)

if __name__ == "__main__":
    main()
