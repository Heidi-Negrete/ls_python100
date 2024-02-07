'''
1.
index - WRONG illegal (reserved keyword). Correct answer is idiomatic. index is not a keyword
CatName - WRONG idiomatic. Correct answer is non-idiomatic. Was thinking valid class name.
lazy_dog - idiomatic
quick_Fox - non-idiomatic (snake case should be all lowercase or all uppercase)
1stCharacter - illegal (cannot begin with numeric character)
operand2 - idiomatic
BIG_NUMBER - WRONG idiomatic. Correct answer is non-idiomatic. was thinking of a constant.
π - non-idiomatic (I guessed but did not know for sure that this was unicode.ASCII is allowed, not unicode.)
'''

'''
Reading the instructions more carefully.  :)
3. 
index - non-idiomatic. lowercase for variables
CatName - non-idiomatic. camelcase is for class names
snake_case - non-idiomatic. lower case for variables
LAZY_DOG3 - idiomatic
1ST - illegal, throws syntax error
operand2 - non-idiomatic, lowercase for variables
BIG_NUMBER - idiomatic
Π - non-idiomatic. not ASCII
'''

'''
4.
index - non-idiomatic (lower case)
CatName - idiomatic
Lazy_Dog - non-idiomatic (does not use snake_case)
1ST - illegal (shouldn't begin with numeric character)
operand2 - non-idiomatic (begins with lowercase)
BigNumber3 - idiomatic
Π - non-idiomatic (not ascii)

'''

# 5 See greeter.py

# 6 See age.py

'''
7.
you will see output:
Good Morning, Victor
Good Afternoon, Victor
Good Evening, Victor
Good Morning, Nina
Good Afternoon, Nina
Good Evening, Nina
- but the souls of all python programmers (past, present, and future) will cry out in pain
'''

# 8
balance = (((((1000 * 1.05) * 1.05) * 1.05) * 1.05) * 1.05)
print(balance)

# 9
balance = 1000
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)

'''
10.
reassignment
mutation WRONG (it's neither because it returns a mutated copy)
mutation WRONG (it's reassignment, the copy you create is assigned to obj)
neither
reassignment
mutation
mutation
mutation
reassignment WRONG (it's neither, basically set returns a new object that is based on object)
reassignment
'''
