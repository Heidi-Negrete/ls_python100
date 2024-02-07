'''
1.
The function receives a dictionary as an argument. It generates a dictionary view object of the keys and then generates a copy of this with the keys sorted alphabetically. The 2nd key is then selected by index and passed through upper function, and this uppercase key string is finally returned: CHRIS
'''


def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()


my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

'''
2.
Way one:
import math as m
print(m.sqrt(37))

Way two:
import math

print(math.sqrt(37))

Way three:
from math import sqrt

print(sqrt(37))

I thought I was being a little snort not implementing my own but this is also official answer phew XD haha
'''


# 3.
def sum_of_squares(num1, num2):
    def square(num):
        return num * num

    return square(num1) + square(num2)


print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# 4.

counter = 0


def increment_counter():
    global counter
    counter += 1


print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101


# 5.
def all_actions():
    counter = 0

    def increment_counter():
        # bug here, should be nonlocal refering to the counter in scope of outer function
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101


all_actions()
