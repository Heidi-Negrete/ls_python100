age = int(input('How old are you? '))
years = [10, 20, 30, 40]

print(f'You are {age} years old.')

for year in years:
    print(f'In {year} years, you will be {age + year} years old.')
