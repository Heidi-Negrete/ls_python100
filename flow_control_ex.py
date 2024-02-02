'''
ternary self-note
x if condition else y
'''

'''
1.

False
True
3
3
False
True
False
False
True  (WRONG. 4 is truthy but RESEARCH)
True

'''

'''
2.
def even_or_odd(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')
'''

'''
3.
code will print:
Product2
Product not found!
'''

'''
4.
if foo():
    return 'bar'
else:
    qux()       

WRONG. return qux(). I was thinking this function would never return and just called qux intentionally, but the ternary would return qux() so it should also be here.
'''

'''
5.
The code will output 'Empty' because the truthy value of an empty list object is False
def is_array_empty(my_list):
    return 'Not Empty' if my_list else 'Empty'


print(is_array_empty([]))
'''

'''
6. 
'''


def capitalize(word):
    return word.upper() if len(word) > 10 else word


'''
7.
'''


def print_range(num):
    if num < 0:
        print(f'{num} is less than 0!')
    elif num <= 50:
        print(f'{num} is between 0 and 50!')
    elif num <= 100:
        print(f'{num} is between 51 and 100!')
    else:
        print(f'{num} is greater than 100!')


print_range(2)
