import pandas as pd

csv_file = '../sample_video_game_sales.csv'

df = pd.read_csv(csv_file)

new_df = df[['Genre', 'Year', 'Name']] # create a new dataframe with only the Genre, Year, and Name columns

access_games_after_2006 = df[df['Year'] > 2006] # create a new dataframe with only the games released after 2006
access_games_after_2006_x = access_games_after_2006[['Genre', 'Year', 'Name']] # create a new dataframe with only the Genre, Year, and Name columns after 2006
xbox360 = df[df['Platform'] == 'X360'] # create a new dataframe with only the games released on Xbox 360
print(df) # print the entire dataframe
print(df.head()) # by default, head() returns the first 5 rows of the dataframe
print(df.head(10)) # returns the first 10 rows of the dataframe
print(new_df) # print the new dataframe with only the Genre column
print(access_games_after_2006) # print the new dataframe with only the games released after 2006
print(access_games_after_2006_x) # print the new dataframe with only the Genre column after 2006
print(df.tail()) # by default, tail() returns the last 5 rows of the dataframe
print(df.tail(10)) # returns the last 10 rows of the dataframe
print(xbox360) # print the new dataframe with only the games released on Xbox 360

