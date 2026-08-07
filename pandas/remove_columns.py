



import pandas as pd

csv_file = '../sample_video_game_sales.csv'

df = pd.read_csv(csv_file)

# Remove columns by name
columns_to_remove = ['Rank', 'Year']
df = df.drop(columns=columns_to_remove)


output_file = '../sample_video_game_sales_modified.csv'
df.to_csv(output_file, index=False)

print(f"Columns {columns_to_remove} removed and saved to {output_file}.")