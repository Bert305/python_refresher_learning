import pandas as pd

# pandas is a powerful library for data manipulation and analysis in Python. It provides two primary data structures: DataFrame and Series.

# uv is an extremely fast, all-in-one Python package and project manager, 

# although currently I'm using virtual env to manage my Python libraries

# example of how to read a CSV file into a pandas DataFrame
# df = pd.read_xlsx('path_to_your_file.xlsx') # Store our Excel file in a DataFrame
# df = pd.read_json('path_to_your_file.json') # Store our JSON file in a DataFrame
# df = pd.read_xml('path_to_your_file.xml') # Store our XML file in a DataFrame

df = pd.read_csv('../pandas/orders.csv') # Store our CSV file in a DataFrame

# print(df) # Display the entire DataFrame
print(df.head()) # Display the first 5 rows of the DataFrame

print(df.tail()) # Display the last 5 rows of the DataFrame


print(df.info()) # Display information about the DataFrame, including column names, data types, and non-null counts

print(df.describe()) # Display summary statistics for numerical columns


print(df.columns) # Display the column names of the DataFrame

print(df['Country']) # Display the 'country' column of the DataFrame

print(df[['Country', 'Product']]) # Display the 'country' and 'product' columns of the DataFrame


print(df.iloc[0]) # Display the first row of the DataFrame

print(df.iloc[1]) # Display the second row of the DataFrame

print(df.iloc[2]['Country']) # Display the third row of the DataFrame and the 'country' column of that row




print(df[df['Country'] == 'USA']) # Display rows where the 'country' column is equal to 'USA'

print(df[df['Category'] == 'Electronics']) # Display rows where the 'Category' column is equal to 'Electronics'

print(df[(df['Category'] == 'Electronics') & (df['Country'] == 'USA')]) # Display rows where the 'Category' column is equal to 'Electronics' and the 'country' column is equal to 'USA'

print(df[(df['Category'] == 'Electronics') | (df['Country'] == 'USA')]) # Display rows where the 'Category' column is equal to 'Electronics' or the 'country' column is equal to 'USA'


print(df[df['Price'] > 100]) # Display rows where the 'Price' column is greater than 100

print(df[df['Quantity'] > 2]) # Display rows where the 'Quantity' column is greater than 2

print(df[df['Quantity'] != 2]) # Display rows where the 'Quantity' column is not equal to 2

print(df[df['CustomerName'].str.startswith('A')]) # Display rows where the 'Customer Name' column starts with the letter 'A'

print(df[df['CustomerName'].str.endswith('a')]) # Display rows where the 'Customer Name' column ends with the letter 'a'


print(df[df['CustomerName'].str.contains('Smith')]) # Display rows where the 'Customer Name' column contains the string 'Smith'

print(df.loc[df['CustomerName'] == 'Anna Ivanova']) # Display rows where the 'Customer Name' column is equal to 'Anna Ivanova'

# Update the 'Product' value for rows where the customer is 'Anna Ivanova'
df.loc[df['CustomerName'] == 'Anna Ivanova', 'Product'] = 10
print(df.loc[df['CustomerName'] == 'Anna Ivanova', 'Product']) # Display the updated Product values for Anna Ivanova