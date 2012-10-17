from __future__ import print_function
import random

numbers = [random.random() for i in range(50000)]

with open('big_data.txt', 'wb') as f:
    for n in numbers:
        print(n, file=f)

with open('big_data_reversed.txt', 'wb') as f:
    for n in numbers[::-1]:
        print(n, file=f)

random.shuffle(numbers)
with open('big_data_shuffled.txt', 'wb') as f:
    for n in numbers:
        print(n, file=f)
