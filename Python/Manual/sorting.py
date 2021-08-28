import csv
import timeit
import operator


file = csv.reader(open('heart.csv', 'r'))


print('''
To Sort Through Choose Bwtween:

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


def sort():
    sortedFile = sorted(file, key=operator.itemgetter(choose))
    for row in sortedFile:
        print(row)


start = timeit.default_timer()


sort()

stop = timeit.default_timer()

print('\nTime: ', stop - start)
