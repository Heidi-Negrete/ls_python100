# First Element

def first(list):
    if list:
        return list[0]
    return None


# Last Element

def last(list):
    if list:
        return list[-1]
    return None


# Add + Delete
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

energy.remove('fossil')
energy.append('geothermal')
print(energy)

# Alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
print(alphabet)

# Filter
scores = [96, 47, 113, 89, 100, 102]
count = 0
for score in scores:
    if score >= 100:
        count += 1
print(count)

# Vocabulary
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated']
]

for category in vocabulary:
    for mood in category:
        print(mood)

# Travel
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']


def contains(element, list):
    for item in list:
        if item == element:
            return True
    return False


# Passcode
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

print('-'.join(passcode))

# Checking items off the grocery list -----  REDO, interpreted the problem incorrectly.
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    print(grocery_list[0])
    del grocery_list[0]

print(grocery_list)
