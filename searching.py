# Sir, I used pandas library

import pandas as pd

df = pd.read_csv("heart.csv")

print(
    'Your options are: [ age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output ]')

key = input('What do you want to search it by? : ')
value = int(input('What is the value? : '))


result = df[df[key] == value]

print(result)
