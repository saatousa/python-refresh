import pandas as pd

data = {
    "customer": ["A", "B", "C", "D", "E", "F"],
    "age": [22, 35, 29, 41, 23, 36],
    "country": ["US", "US", "UK", "UK", "US", "UK"],
    "purchases": [1, 5, 3, 2, 8, 4],
    "spent": [100, 500, 300, 200, 900, 450]
}

df = pd.DataFrame(data)

# Part 1 — Basic insight
# print(df.head())
# print(df.describe())

# Average spending per customer
# 408.33333

# Most active customer (by purchases)
active_customer = df["purchases"].max()
# print(df.loc[df["purchases"] > active_customer])

# Highest spender
highest_spender = df["spent"].max()
# print(df.loc[df["spent"] > highest_spender])


# Part 2 — Group thinking
# Which country spends more on average?
# print(df.groupby("country")["spent"].mean())
# US spends more on avg

# Which country has more purchases on average?
print(df.groupby("country")["purchases"].mean())
# US has more purchases on avg


# convert PANDAS to SQL
# df[df["spent"] > 300]
# SELECT *
# FROM data
# WHERE spent > 300

