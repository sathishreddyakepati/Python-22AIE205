import pandas as pd

# s = pd.Series([10, 20, 30 ,40])
# print(s)
# data ={
#     "name":["A", "B", "C"],
#     "marks":[80,90,75]
# }
# df = pd.DataFrame(data)
# print(df)

df = pd.read_csv("students.csv")
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.sort_values("marks",ascending=False))
# print(df["marks"].value_counts())
print(df.groupby("department")["marks"].mean())