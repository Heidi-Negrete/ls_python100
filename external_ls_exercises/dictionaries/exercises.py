# First Car

car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80000,
}

# Adding the Year
car['year'] = 2003

# Broken Odometer
del car['mileage']

# What Color?
print(car['color'])

# What's my length?
print(len(car))

# Checking Key Existence
student = {
    'id': 123,
    'grade': 'B',
}
# if you want to see whether both are or not
print('name' and 'grade' in student)
print('name' in student)
print('grade' in student)


# Multiple Cars
cars = {
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'mileage': 80000,
    },
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998,
    },
}

# Which Collection?

car = [['type', 'sedan'], ['color', 'blue'], ['year', 2003]]

# Divided by Two
numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}
half_numbers = [num // 2 for num in numbers.values()]
print(half_numbers)

# Labeled Numbers

for key, value in numbers.items():
    print(f'A {key} number is {value}.')
