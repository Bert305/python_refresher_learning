import pandas as pd

csv_file = '../sample_video_game_sales.csv'

df = pd.read_csv(csv_file)

new_df = df[['Genre', 'Year', 'Name']] # create a new dataframe with only the Genre, Year, and Name columns
print(df) # print the entire dataframe
print(df.head()) # by default, head() returns the first 5 rows of the dataframe
print(df.head(10)) # returns the first 10 rows of the dataframe
print(new_df) # print the new dataframe with only the Genre column

