

import pandas as pd

csv_file = '../sample_video_game_sales.csv'

df = pd.read_csv(csv_file)

# Transform DataFrame to JSON
json_output = df.to_json(orient='records', lines=True)

# pretty the json with square brackets
json_output = '[\n' + ',\n'.join(json_output.splitlines()) + '\n]'

output_file = '../sample_video_game_sales.json'
with open(output_file, 'w') as f:
    f.write(json_output)

print(f"Data transformed to JSON and saved to {output_file}.")