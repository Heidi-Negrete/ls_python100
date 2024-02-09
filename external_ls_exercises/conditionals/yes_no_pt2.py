import random

random_number = random.randint(0, 1)

# more succinctly: print('Yes!' if random number else 'No')
print('Yes!') if random_number else print('No.')
