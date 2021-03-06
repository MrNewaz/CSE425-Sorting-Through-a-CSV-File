# Sir, I used pandas library

import pandas as pd
import timeit


df = pd.read_csv("heart.csv")

print(
    'Your options are: [ age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall, output ]')

key = input('What do you want to sort it by? : ')

start = timeit.default_timer()

# Your statements here


sorted_df = df.sort_values(by=[key], ascending=True)


print(sorted_df)

stop = timeit.default_timer()

print('Time: ', stop - start)


new_file = input('Do you want to output it into a file? (yes/no) ')

if new_file == 'yes':
    sorted_df.to_csv(f'heart_sorted_by_{key}.csv', index=False)
