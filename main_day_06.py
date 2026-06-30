import pandas as pd

data = {
    "name": ["Sara", "John", None, "David", "Mike"],
    "department": ["HR", "IT", "IT", None, "Sales"],
    "salary": [50000, None, 55000, 70000, 65000],
    "age": [25, 30, None, 35, 32]
}

df = pd.DataFrame(data)
# print(df.isnull())
# print(df.isnull().sum())
# print(df.notnull())
# print(df.isna())
# print(df.isna().values.any())

# df_clean = df.dropna()
# print(df_clean)

df["salary"] = df["salary"].fillna(df["salary"].mean())
df["department"] = df["department"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].mean())

print(df)

