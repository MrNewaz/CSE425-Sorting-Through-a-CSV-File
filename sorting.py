import pandas as pd


df = pd.read_csv("heart.csv")

key = input('What do you want to sort it by? ')

sorted_df = df.sort_values(by=[key], ascending=True)


print(sorted_df)


new_file = input('Do you want to output it into a file? (yes/no) ')

if new_file == 'yes':
    sorted_df.to_csv(f'heart_sorted_by_{key}.csv', index=False)
