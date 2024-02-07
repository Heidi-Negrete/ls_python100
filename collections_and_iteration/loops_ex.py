# study focus on comprehensions. expression for element in iterable if condition

# 1. counter is never changed in the body of the loop and will never be >= 5

# 2. see age.py

# 3
import random

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for num in my_list:
    print(num)

# 4
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

for num in my_list:
    if num % 2 != 0:
        print(num)

# 5.
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for list in my_list:
    for num in list:
        if num % 2 == 0:
            print(num)

# 6
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []

for num in my_list:
    if num % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)

# 7


def find_integers(x):
    return [element for element in x if type(element) == int]


# 8
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

answer = {key: len(key) for key in my_set if len(key) % 2 != 0}

print(answer)

# 9


def calc_factorial(num):
    factorial = 1
    index = 1
    while index <= num:
        factorial *= index
        index += 1
    return factorial


print(calc_factorial(1))
print(calc_factorial(25))

# 10

highest = 10

while True:
    number = random.randrange(highest + 1)
    print(number)  # dont forget to print the number
    if number == highest:
        break

# 11
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

index = 0

while index < len(my_list):
    count = 0
    while count < len(my_list[index]):
        if my_list[index][count] % 2 == 0:
            print(my_list[index][count])
        count += 1
    index += 1
# I should have used inner_index and outer_index like in the solutions to avoid confusion yikes
