# panda.py
import pandas as pd

# simple DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85.5, 90.0, 78.5]
})

print("DataFrame:\n", df)

# summary statistics describe te da la mayorias de estadisticas de cualquier data frame
print("\nDescribe:\n", df.describe())

# select a column
print("\nAges:\n", df["Age"])

# filter rows
print("\nAge > 28:\n", df[df["Age"] > 28])
