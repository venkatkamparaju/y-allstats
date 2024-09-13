import pandas as pd

def analyze_spreadsheet(file_path):
    """Analyzes statistical values in a spreadsheet.

    Args:
        file_path (str): The path to the spreadsheet file.

    Returns:
        pandas.DataFrame: A DataFrame containing the statistical analysis.
    """

    # Read the spreadsheet into a DataFrame
    df = pd.read_csv(file_path)

    # Calculate statistical values
    mean = df.mean()
    median = df.median()
    mode = df.mode().iloc[0]
    variance = df.var()
    std_dev = df.std()
    range_ = df.max() - df.min()
    correlation = df.corr()

    # Create a DataFrame to store the results
    results = pd.DataFrame({
        'Mean': mean,
        'Median': median,
        'Mode': mode,
        'Variance': variance,
        'Standard Deviation': std_dev,
        'Range': range_,
        'Correlation': correlation
    })

    return results

# Replace 'your_spreadsheet.csv' with the actual path to your file
file_path = 'your_spreadsheet.csv'
results = analyze_spreadsheet(file_path)

print(results)
