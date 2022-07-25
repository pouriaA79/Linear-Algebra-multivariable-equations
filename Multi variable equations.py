import numpy as np
# variables
zarib = []
zaribb1 = 0
number = 100
pivots = {}
pivot = {}
count = 0
Notfree = []
free = []
flag = False
zarayebfreeha = []
adad = 1
sabet = string = ''
flag_row1 = False

numbers = input('enter the row number and column number: ')
numbers = numbers.split(" ")
row_num = int(numbers[0])
col_num = int(numbers[1])
# get row info
for i in range(row_num):
    print('enter row ' + str(1 + i))
    zarib += input().split(" ")

constant = input('enter constant:').split(" ")

for i in range(len(zarib)):
    zarib[i] = float(zarib[i])

for j in range(len(constant)):
    constant[j] = float(constant[j])
# make our matrix

zarib = np.array(zarib[:]).reshape(row_num, col_num)
constant = np.array(constant).reshape(-1, 1)
zarib = np.hstack((zarib, constant))
print("given matrix:")
print(zarib)
change = False
# find pivots and make matrix echelon form
for i in range(col_num):

    for j in range(row_num - count):
        if change == False:
            if zarib[j + count, i] != 0.0:
                flag = True
                number = count + j
            if number == i:
                flag_row1 = True
                change = True
                pivots[i + 1] = [count, i]
                pivot[count + 1] = [count, i]
            if flag == True and flag_row1 == False:
                pivots[i + 1] = [count, i]
                pivot[count + 1] = [count, i]
                zarib[[j + count, count]] = zarib[[count, j + count]]
                change = True

    if change == True:
        count = count + 1
        for k in range(row_num - count):
            if zarib[count + k, i] != 0:
                zaribb1 = (-1) * (zarib[count + k, i] / zarib[count - 1, i])

                zarib[k + count] = zarib[k + count] + zaribb1 * zarib[count - 1]
    flag = False
    change = False
    flag_row1 = False
    number = 100
# make matrix reduced echelon form
for i in reversed(range(len(pivot) + 1)):
    if i != 0:
        for j in reversed(range(pivot[i][0])):
            if zarib[j, pivot[i][1]] != 0:
                zaribb2 = (-1) * (zarib[j, pivot[i][1]] / zarib[pivot[i][0], pivot[i][1]])
                zarib[j] = zarib[j] + zaribb2 * zarib[pivot[i][0]]

for i in range(col_num):
    free.append(i + 1)

Notfree = pivots.keys()

free = [i for i in free if i not in Notfree]

# find answers
for i in range(col_num):
    if 1 + i in free:
        print('x' + str(i + 1) + ' is free')
    elif i + 1 in Notfree:
        for j in range(col_num):

            if (zarib[pivots[i + 1][0], pivots[i + 1][1]]) != 0:
                if (j == pivots[i + 1][1]):
                    name = 'x' + str(j + 1) + ': '
                    adad = -1 / (1 * zarib[pivots[i + 1][0], pivots[i + 1][1]])

                else:
                    if adad * zarib[pivots[i + 1][0], j] > 0:
                        string = string + '+' + str(adad * zarib[pivots[i + 1][0], j]) + 'x' + str(j + 1)
                    elif adad * zarib[pivots[i + 1][0], j] < 0:
                        string = string + str(adad * zarib[pivots[i + 1][0], j]) + 'x' + str(j + 1)
                if j == col_num - 1:
                    if adad * zarib[pivots[i + 1][0], col_num] >= 0:
                        sabet = str(-1 * adad * zarib[pivots[i + 1][0], col_num])
                    elif adad * zarib[pivots[i + 1][0], col_num] < 0:
                        sabet = str(-1 * adad * zarib[pivots[i + 1][0], col_num])
        string = name + sabet + string
        print(string)
        string = ''