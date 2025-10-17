





# data visualization and analysis project of job industries and will generate a csv file and visualizations
# of a pie, bar, and line graph



import pandas as pd
import os

# Load your DataFrame from a CSV file (update the path as needed)
# Get the directory of the current script and build absolute path to the CSV file
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, '..', 'jobs_april_may_2025.csv')
df = pd.read_csv(input_path)

# Clean and process the 'Job Title Industry' column
industry_counts = df['Job Title Industry'].value_counts().reset_index()
industry_counts.columns = ['Job Title Industry', 'Count']

# Calculate percentage
total = industry_counts['Count'].sum()
industry_counts['Percentage'] = (industry_counts['Count'] / total * 100).round(2)

# Save to CSV in the current directory (job_analysis)
output_path = 'job_industry_counts_and_percentages3.csv'
industry_counts.to_csv(output_path, index=False)

# import ace_tools as tools; tools.display_dataframe_to_user(name="Job Industry Counts and Percentages", dataframe=industry_counts)

import matplotlib.pyplot as plt

# Pie chart of job title industry counts and percentages
plt.figure(figsize=(8, 8))
plt.pie(
    industry_counts['Count'],
    labels=industry_counts['Job Title Industry'],
    autopct='%1.1f%%',
    startangle=140
)
plt.title('Job Title Industry Distribution')
plt.tight_layout()
plt.show()

# Bar chart of counts by industry
plt.figure(figsize=(10, 6))
plt.bar(industry_counts['Job Title Industry'], industry_counts['Count'], color='C0')
plt.xlabel('Job Title Industry')
plt.ylabel('Count')
plt.title('Job Title Industry Counts')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Line graph of percentage by industry
plt.figure(figsize=(10, 6))
plt.plot(industry_counts['Job Title Industry'], industry_counts['Percentage'], marker='o', linestyle='-',
         color='C1')
plt.xlabel('Job Title Industry')
plt.ylabel('Percentage (%)')
plt.title('Job Title Industry Percentage')
plt.xticks(rotation=45, ha='right')
# Annotate percentage values above points
for i, v in enumerate(industry_counts['Percentage']):
    plt.text(i, v + 0.5, f"{v}%", ha='center', va='bottom', fontsize=8)
plt.tight_layout()
plt.show()



output_path
