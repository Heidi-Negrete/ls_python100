'''
1.
my_object1 == my_object2  This statement is checking equivalance between the value of two objects.,
my_object1 is my_object2    This statement is checking if the objects identity is the same, that is if they reference the same object in memory.
'''

# 2. {42, 'Monty Python', ('a', 'b', 'c'), 5, 6, 7, 8, 9} - because both variables reference the same object any changes to the first variable will be seen if you print the object using the second variable. WRONG range(5,10) will not be unpacked.

# 3. 'The Life of Brian' - because using dict() creates a copy of the dict.

# 4. [1, 42, 3] - because nested lists are shallow copied even though dict() is used. dict1['a'] references the same object as dict2['a']

# 5.
import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

# All of these should print False
print(dict1 is dict2)
print(dict1['a'] is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b'] is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

'''
6.
False
True
True
True
True
True
True
'''
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1 is dict2)
print(dict1['a'] is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b'] is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
