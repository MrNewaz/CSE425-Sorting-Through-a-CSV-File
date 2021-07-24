import pandas as pd

df = pd.read_csv("heart.csv")

result = df[df['age'] == 63]

print(result)
