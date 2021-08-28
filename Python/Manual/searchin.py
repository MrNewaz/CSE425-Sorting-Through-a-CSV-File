import csv
import timeit


file = csv.reader(open('heart.csv', 'r'))


print('''
To Search From Choose Bwtween:

Enter: 0, for age
Enter: 1, for sex
Enter: 2, for cp
Enter: 3, for trtbps
Enter: 4, for chol
Enter: 5, for fbs
Enter: 6, for restecg
Enter: 7, for thalachh
Enter: 8, for exng
Enter: 9, for oldpeak
Enter: 10, for slp
Enter: 11, for caa
Enter: 12, for thall
Enter: 13, for output
''')

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
