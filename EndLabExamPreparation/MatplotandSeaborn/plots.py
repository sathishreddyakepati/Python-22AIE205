import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# df = pd.read_csv("students.csv")

# plt.hist(df["marks"])
# plt.show()

# plt.bar(df["name"], df["marks"])
# plt.show()

# plt.scatter(df["hours"], df["marks"])
# plt.show()
# marks = [45, 50, 52, 55, 58, 60, 62, 65, 70, 95]
data  = {
    "marks":[45, 50, 52, 55, 58, 60, 62, 65, 70, 95]
}
df = pd.DataFrame(data)
sns.boxplot(x=df["marks"])
plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()