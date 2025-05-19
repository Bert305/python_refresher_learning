










import pandas as pd

# Load your DataFrame from a CSV file (update the path as needed)
input_path = '../jobs_april_may_2025.csv'  # <-- Change this to your actual CSV file path
df = pd.read_csv(input_path)

# Clean and process the 'Job Title Industry' column
industry_counts = df['Job Title Industry'].value_counts().reset_index()
industry_counts.columns = ['Job Title Industry', 'Count']

# Calculate percentage
total = industry_counts['Count'].sum()
industry_counts['Percentage'] = (industry_counts['Count'] / total * 100).round(2)

# Save to CSV
output_path = '../job_analysis/job_industry_counts_and_percentages.csv'
industry_counts.to_csv(output_path, index=False)

# import ace_tools as tools; tools.display_dataframe_to_user(name="Job Industry Counts and Percentages", dataframe=industry_counts)

output_path
