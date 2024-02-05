# 1. len(people)
# 2. stuff = ('hello', 'world', 'goodbye', 'now')
'''
3.
Differences:
    lists are mutable - tuples are immutable
    (Add from solutions: list literals use [] and tuple literals use () agh! xD)
Similarities:
    lists are ordered - so are tuples
    lists are iterable - so are tuples
    (Add from solutions: both sequences, ordered collections that can use numeric indexes to access members. Heterogenous, elements of many types allowed)
'''

# 4. because a string object is made up of ordered sequence of char (access individual chars with indexing)

# 5. set types differ from sequence because they are unordered

# 6. str_pi = str(pi)

'''
7.
0,1,2,3,4,5,6
1,2,3,4,5
3,7,11
~~7,6,5,4,3~~ WRONG if working negative starting value should be bigger than stop value: empty range
~~2,3,4,5,6,7,8~~WRONG start from start value and move negatively: 8,7,6,5,4
'''

# 8. print(list(range(3,17,4)))

'''
9.
    1. Yes. list(my_list) returns an exact copy of my_list and assigns it to another_list
    2. No. it was a copy not the same object
    3. Yes. because the copy was exact, the elements are the same.
    4. Yes. Nested collections constructed by list are 'shallow copies' and reference the same object
'''

# 10. Because the {} indicates that this collection is a set, you cannot expect the code to print the elements in any specific order, as sets are unordered.

# 11
countries_dict = {
    "Alice": "USA",
    "Francois": "Canada",
    "Inti": "Peru",
    "Monika": "Germany",
    "Sanyu": "Uganda",
    "Yoshitaka": "Japan",
}
print(countries_dict["Inti"])
