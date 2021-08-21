# Sir, I used pandas library

import pandas as pd
import timeit

df = pd.read_csv("heart.csv")

print(
    'Your options are: [ age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output ]')

key = input('What do you want to search it by? : ')
value = int(input('What is the value? : '))

start = timeit.default_timer()

result = df[df[key] == value]

print(result)


stop = timeit.default_timer()

print('Time: ', stop - start)
