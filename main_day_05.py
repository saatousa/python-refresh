import pandas as pd

df = pd.read_csv("employees.csv")

# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())

# 1. What is the average salary?
# print(df["salary"].mean())

# 2. Who is the oldest employee?
# result = df[df["age"] == 35]
# print(result["name"])

# 3. How many employees are in each department?
each_department = df.groupby("department").count()
# print(each_department)

# 4. Which department has the highest average salary?
highest_avg_salary = df.groupby("department").agg({"salary": pd.Series.mean})
print(highest_avg_salary)

# 5. List employees earning more than 55,000.
result = df[df["salary"] > 55000]
# print(result["name"])
