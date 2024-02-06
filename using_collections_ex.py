# 1.
print(range(0, 25, 3)[6])

# 2
school = 'Launch School'
print(school[school.find('c'):])

# 3
origin_tuple = (1, 2, 3, 4, 5)
# this is really unreadable. refactor start and stop into their own variables perhaps.
my_tuple = origin_tuple[(len(origin_tuple) - 2):0:-1]
print(my_tuple)

# 4
pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

'''
5.
['a', 'b'] cannot be used because a list is mutable and therefore not a 'hashable' value
{'a': 1, 'b': 2} cannot be used because a dict is mutable and therefore not a 'hashable' value
{1,4,9,16,25} a set also (same reasons)
'''

'''
6.
False
False
False
False
False
True
True
False
False
False
False
'''

# 7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# unreadable, refactor if doing this way
chapter_knowledge_only = '+'.join(info.split(':'))

# alternate method
replacement_string = info.replace(':', '+')

print(chapter_knowledge_only)
print(replacement_string)


# 8 in line three, rfind is returning an index relative to the substring of text defined by the splice notation, whereas in 4 rfind is looking at index 21 - 35 and returning an index relative to the whole string.

# 9
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606

# 10
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            }
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            }
        },
    }
}
print(cats['Pete']['Cocoa']['enjoys'])

'''
11.
False
True
True
False
True
False
False
True
True - WRONG. in with sets only checks whether a specific value is in the set 
True
'''

'''
12.
print(3 in x) # where x is your list
'''

'''
13.
True
True - WRONG - study. 'in' in the context of lists is looking not for substring but for a matching element.
True
False
'''

# 14
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

my_mega_list = list(zip(my_str, my_list, my_tuple, my_range))
print(my_mega_list)

'''
15.
['Cat','Bird','Snake']

(keys makes a shallow copy) - WRONG understanding, dict.keys() returns a dictionary view object
'''
