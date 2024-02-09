weather = 'sun-shower'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case 'tornado':
        print('Seek shelter! Tornado warning!')
    case 'sun-shower':
        print("It's a gorgeous sun shower let's play in the rain!")
    case 'snowy':
        print("It's snowing. Sip some hot cocoa with me.")
    case _:
        print("Let's stay inside.")
