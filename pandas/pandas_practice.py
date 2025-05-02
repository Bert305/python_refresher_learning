import pandas as pd

csv_file = '../sample_video_game_sales.csv'

df = pd.read_csv(csv_file)
print(df) # print the entire dataframe
print(df.head()) # by default, head() returns the first 5 rows of the dataframe
print(df.head(10)) # returns the first 10 rows of the dataframe

