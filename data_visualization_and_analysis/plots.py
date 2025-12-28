import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame for demonstration

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

columns = [
    "symboling","normalized-losses","make","fuel-type","aspiration",
    "num-of-doors","body-style","drive-wheels","engine-location",
    "wheel-base","length","width","height","curb-weight","engine-type",
    "num-of-cylinders","engine-size","fuel-system","bore","stroke",
    "compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"
]

df = pd.read_csv(url, names=columns)

# Define x and y for line plot - showing only first 25 data points
x = df.index[:25]
y = df["price"][:25]

# Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot (First 25 Cars)")
plt.xlabel("Car Index")
plt.ylabel("Price")
plt.show()


# Scatter Plot
plt.figure()
plt.scatter(df["engine-size"][:25], df["price"][:25])
plt.title("Engine Size vs Price (First 25 Cars)")
plt.xlabel("Engine Size")
plt.ylabel("Price")
plt.show()


# Histogram
plt.figure()
plt.hist(df["price"][:10], bins=5, edgecolor="black")
plt.title("Price Distribution (First 10 Cars)")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()


#Bar Plot
counts = df["drive-wheels"].value_counts()

plt.figure()
plt.bar(counts.index, counts.values)
plt.title("Count by Drive Wheels")
plt.xlabel("Drive Wheels")
plt.ylabel("Count")
plt.show()



