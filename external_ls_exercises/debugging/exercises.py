'''
Reading Error Messages

too many arguments, 1 expected. when calling the function, you should pass in the numbers in some iterable collection such as a list or tuple. - Correction/clarification: "TypeError" takes 1 positional argument but 6 were given.

WRONG - I did not catch the second error until the first was corrected and I attempted to pass in values as an iterable. I tested set rather than using the obvious list. Works fine for the first set of numbers, but set() requires an iterable argument, and a single int is not. 'sjkd' strings are though, in contrast.
'''

# Weather Forecast    - simply have the items True and False in the list rather than the strings 'True' and 'False'

# Multiply By 5       - the input from user is of string type. convert with int() before passing in to the function!


# Pets
import copy
pets = {'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar'}

pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}


# Confucius Says
# the problem is the function does not return anything. add return to each match case
def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'


print('Confucius says:')
print('"' + get_quote('Confucius') + '"')


# Populate List --- Fix by adjusting range to start at 1 and end at 5 with range(1,6)

# Dictionary Access
info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'Unknown'))

# Matrix

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    # matrix.append(copy.deepcopy(sub_list)) - This is excessive.making a copy of sublist is enough since the sublist doesn't have any nested elements of it's own.
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix)  # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


# Find Maximum

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

# Digit Product


def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product


result = digit_product('12345')
print(result)  # expected: 120, actual: 0
