import csv
import timeit


file = csv.reader(open('heart.csv', 'r'))


print('Enter: 0, for age')
print('Enter: 1, for sex')
print('Enter: 2, for cp')
print('Enter: 3, for trtbps')
print('Enter: 4, for chol')
print('Enter: 5, for fbs')
print('Enter: 6, for restecg')
print('Enter: 7, for thalachh')
print('Enter: 8, for exng')
print('Enter: 9, for oldpeak')
print('Enter: 10, for slp')
print('Enter: 11, for caa')
print('Enter: 12, for thall')
print('Enter: 13, for output')

choose = int(input("Your choice: "))
value = input("What value do you want to search by? : ")


def search():

    total = 0

    for row in file:
        if value.lower() in row[choose].lower():
            print(row)
            total = total + 1

    print('\nTotal ' + str(total) + ' results found')


start = timeit.default_timer()


search()

stop = timeit.default_timer()

print('Time: ', stop - start)
