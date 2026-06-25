# PANDAS

import pandas as pd



data = {
    "name": ["Sara", "John", "Emma", "David"],
    "age": [25, 30, 28, 35],
    "salary": [50000, 60000, 55000, 70000]
}

df = pd.DataFrame(data)

# print(df)

# print(df["name"])
# print(df["salary"])

# print(df["salary"].max())
# print(df["salary"].min())
# print(df["salary"].mean())

# older_than_28= df[df["age"] > 28]
# print(older_than_28["name"])

# salary_over_50k = df[df["salary"] > 50000]
# print(salary_over_50k["name"])

df["bonus"] = df["salary"] / 10
print(df)