#Q1

f = input('Enter the file name:')

n = int(input('No. of last lines to read:'))

try:

    with open(f) as filepointer:

        print('Read last', n, 'lines from file:', f)

        for line in (filepointer.readlines()[-n:]):
            # -n means it read from last.

            # last line means -1,second last line means -2and so on

            print(line, end='')

except:

    print('file no exist')

#Q2

file = open("test.txt")
wordcount = {}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for a, b in wordcount.items():
    print(a, b)

#Q3

with open("test.txt") as f:
    with open("test2.txt", "w") as f1:
        for i in f:
            f1.write(i)

#Q4

with open('test.txt') as f1, open('test1.txt') as f2:
    for line1, line2 in zip(f1, f2):
        # line1 from test.txt, line2 from test2.txt
        print(line1 + line2)

#Q5

import random

f = open("test3.txt", "w+")


def Rand():
    x = []
    for i in range(10):
        x.append(random.randint(1, 1000))
    return x


random_numbers = ((Rand()))
f.write(str(random_numbers))
f.read()
f.close()
sorted_numbers = sorted(random_numbers)
f1 = open("test4.txt", "w+")
f1.write(str(sorted_numbers))
f1.close()