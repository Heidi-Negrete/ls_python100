'''
1. 
def set_foo():
    foo = 'bar'

set_foo()
print(foo)

This will raise an undefined error because foo is scoped to set_foo and cannot be passed to print
'''

'''
2.
foo = 'bar'


def set_foo():
    foo = 'qux'


set_foo()
print(foo)

This program will print bar because the foo inside set_foo only shadows the foo'bar' and the foo passed to print will use foo in the same scope
'''

# 3


def multiply(x, y):
    return x * y


first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
print(f'{first} * {second} = {multiply(first, second)}')

'''
4.
function name = multiply_numbers
function arguments = 2, 3, and 4
function definition = the first 3 lines of the code
function body = lines 2 and 3
function parameters = num1, num2, and num3
function invocation = on line 5 "multiply_numbers(2,3,4)"
function return value = result (line 5)  // maybe wrong? the result of running code will be 24, but instructions were to 'identify the following items in that code'. Not sure if result can be referred to as the return value of the function in the definition.
all identifiers = multiply_numbers, num1, num2, num3, result, product
'''

# 5. nothing, because there is no call to print.

# 6. nothing, because the call to print is after the return in the function definition which means it will never be called.

# 7. raise an error, because the function requires two arguments and only 1 is provided.

# 8. raise an error, because too many arguments provided

'''
9. It will print:
42
3.141592
2.718
'''

'''
10. It will print:
42
3.141592
2
'''

'''
11. It will print:
42
3
2
'''

# 12. It will raise an error, because at least one argument is required.

# 13. It will raise an error, because once you define a parameter as optional, all parameters defined after it need to also have a default value.

'''
14. 
    1 - multiply, left, right
    2 - left, right
    4 - get_num, prompt
    5 - float, input, prompt
    7 - first_number, get_num
    8 - second_number, get_num
    9 - product, multiply, first_number, second_number
    10 - print, first_number, second_number, product
'''

'''
15.
multiply - global
left - local
right - local
get_num - global
float - built-in
input - built-in
prompt - local
first_number - global
second-number - global
product - global
print - built-in

'''

'''
16.
function names:
    multiply 1,9
    get_num 4,7,8
    float 5
    input 5
    print 10

parameters:
    left 1
    right 1
    prompt 4
'''

'''
17.
function names: say, input, max, upper, lower, print
method names: upper, lower
built-in functions: max, print, input
'''

'''
18.
print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))
'''

'''
19.
print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
'''
