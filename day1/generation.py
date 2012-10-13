from __future__ import print_function
import random

numbers = [random.random() for i in range(10000)]

with open('data.txt', 'wb') as f:
    for n in numbers:
        print(n, file=f)

with open('data_reversed.txt', 'wb') as f:
    for n in numbers[::-1]:
        print(n, file=f)

random.shuffle(numbers)
with open('data_shuffled.txt', 'wb') as f:
    for n in numbers:
        print(n, file=f)
