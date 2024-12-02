### Pareto Chart Analysis: A Comprehensive Guide

#### 1. Purpose and Use Cases

**When to Use Pareto Charts:**
- To visualize the frequency of defects or issues
- To identify the "vital few" causes that contribute to most problems
- To prioritize improvement efforts
- To demonstrate the cumulative impact of different factors
- When applying the 80/20 principle to quality improvement

**Suitable Data Types:**
1. **Frequency Data:**
   - Defect counts
   - Error occurrences
   - Quality issues
   - Customer complaints

2. **Categorical Variables:**
   - Defect types
   - Error categories
   - Process steps

#### 2. Code Structure and Implementation

##### Core Function: create_pareto()
```python
def create_pareto(data, title="Pareto Chart", figsize=(10, 6)):
    """Creates a Pareto chart from frequency data"""
    sorted_data = data.sort_values(ascending=False)
    total = sorted_data.sum()
    cumulative_percent = np.cumsum(sorted_data) / total * 100
```
**Purpose:**
- Creates dual-axis visualization
- Combines bar chart (frequencies) with line plot (cumulative percentages)
- Handles data sorting and percentage calculations

##### Data Loading and Preprocessing
```python
data_folder = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
data_file = os.path.join(data_folder, 'DEFECT TYPES.CSV')
defect_data = pd.read_csv(data_file)
```
**Features:**
- Uses relative path navigation
- Ensures cross-platform compatibility
- Loads defect type data from CSV

#### 3. Analysis Methods

##### Method 1: Pre-summarized Data
```python
defect_freq = pd.Series(data=defect_data['Occurrences'].iloc[:10].values,
                       index=defect_data['Defect'].iloc[:10].values)
```
**Analysis Provided:**
- Uses pre-calculated frequency counts
- Limited to top 10 defects
- Maintains original defect labels

##### Method 2: Raw Data Analysis
```python
freq_table = defect_data['Coded Defects'].value_counts()
```
**Analysis Provided:**
- Calculates frequencies directly from raw data
- Includes all defect types
- More flexible for different analyses

#### 4. Shift-based Analysis

**Implementation:**
```python
shifts = defect_data['Shift'].unique()
fig, axes = plt.subplots(1, len(shifts), figsize=(15, 5))
```
**Features:**
- Creates separate Pareto charts for each shift
- Allows comparison across shifts
- Maintains consistent scale and format

#### 5. Defect Type Mapping

```python
defect_mapping = {
    1: "Double Edges",
    2: "Excess Material",
    # ... more mappings ...
}
```
**Purpose:**
- Converts numeric codes to descriptive labels
- Improves chart readability
- Facilitates interpretation

#### 6. Visualization Components

**Key Elements:**
1. **Bar Chart:**
   - Heights represent frequencies
   - Color: lightcoral
   - Left y-axis scale

2. **Line Plot:**
   - Shows cumulative percentages
   - Color: navy
   - Right y-axis scale
   - Includes markers for each point

3. **Formatting:**
   - Rotated x-axis labels (45 degrees)
   - Grid lines for readability
   - Tight layout for proper spacing
   - Twin axes for dual scales

#### 7. Analysis Capabilities

1. **Overall Distribution:**
   - Identifies most frequent defects
   - Shows relative importance
   - Reveals cumulative impact

2. **Shift Analysis:**
   - Compares patterns across shifts
   - Identifies shift-specific issues
   - Enables targeted improvement

3. **Label Management:**
   - Supports both coded and descriptive labels
   - Flexible mapping system
   - Maintains data integrity

#### 8. Best Practices Implemented

1. **Code Organization:**
   - Modular function design
   - Clear parameter documentation
   - Consistent naming conventions

2. **Data Handling:**
   - Proper path management
   - Flexible data input options
   - Error handling considerations

3. **Visualization:**
   - Professional appearance
   - Clear labeling
   - Appropriate color choices
   - Readable text and scales

#### 9. Common Applications

1. **Manufacturing:**
   - Defect analysis
   - Quality improvement
   - Process optimization

2. **Quality Control:**
   - Issue prioritization
   - Resource allocation
   - Impact assessment

3. **Process Improvement:**
   - Problem identification
   - Root cause analysis
   - Performance monitoring