import pandas as pd

data = {
    "customer": ["A", "B", "C", "D", "E", "F"],
    "age": [22, 35, 29, 41, 23, 36],
    "country": ["US", "US", "UK", "UK", "US", "UK"],
    "purchases": [1, 5, 3, 2, 8, 4],
    "spent": [100, 500, 300, 200, 900, 450]
}

df = pd.DataFrame(data)
# print(df)


# Part 1 - Answer with code
# Total revenue (spent)
total_revenue = df["spent"].sum()
# print(total_revenue)

# Average number of purchases
avg_purchases = df["purchases"].mean()
# print(avg_purchases)

# Youngest customer
youngest_customer = df["age"].min()
# print(youngest_customer)

# Oldest customer
oldest_customer = df["age"].max()
# print(oldest_customer)


# Part 2 — Find patterns
# Do older customers tend to spend more?
# print(df.sort_values(by="age", ascending=False))
# Age and spending habit has no correlation because as we can see the oldest customer spent 200 while someone 23 which in our data doesnt count as the youngest spent 900

# Do customers who purchase more frequently also spend more?
# print(df.sort_values(by="purchases", ascending=False))
# Yes according to data we can see that the more purchases made the more a person has spent 


# Part 3 — Add a new column
df["average_per_purchase"] = df["spent"]/ df["purchases"]
print(df)


# Perfect.

# The only thing missing was answering:

# Who spends the most per purchase?

# Did you calculate it?

# If not, go back and find that person. It should only take a minute, and it's good practice.