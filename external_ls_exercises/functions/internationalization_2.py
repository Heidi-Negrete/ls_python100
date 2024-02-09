greetings = {
    'en': {
        'US': 'Hey!',
        'GB': 'Hello!',
        'AU': 'Howdy!',
    },
    'fr': 'Salut!',
    'pt': 'Olá!',
    'de': 'Hallo!',
    'sv': 'Hej!',
    'af': 'Haai!',
}


def local_greet(locale):
    lang = locale.split('_')[0]
    country = locale.split('_')[1].split('.')[0]

    greeting = greetings.get(lang)
    if not greeting:
        return 'Your language isn\'t available, but we offer you a warm welcome!'

    elif lang == 'en':
        return greetings[lang][country]
    else:
        return greetings[lang]


# tests
print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_EFEEFE.EUIFLEE'))  # Salut!

# polite greeting, language not available
print(local_greet('as_djkfl;jasdklf;j'))
