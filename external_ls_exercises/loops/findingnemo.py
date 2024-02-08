fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break


'''
With a while loop (could have done this without the found variable but it felt poetic, and its inefficient anyway might as well go all out~):

index = 0
found = False
while found != True:
    fish = fish_list[index]
    print(fish)
    index += 1
    if fish == 'Nemo':
        found = True
'''
