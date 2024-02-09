'''
# length
my_string = 'These aren\'t the droids you\'re looking for.'

print(len(my_string))
'''

'''
# ALL CAPS
my_string = 'confetti floating everywhere'
print(my_string.upper())
'''

'''
# Ignoring Case

name = 'Roger'
if name.lower() == 'RoGeR'.lower():      # WRONG. Use casefold. some languages have inconventional methods of conversion
    print('true')
else:
    print('false)
'''

# Multiline String
rhmye = '''A pirate I was meant to be!
Trim the sails and roam the sea!'''

# Contains Character
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
# print('x' in char_sequence)


'''
# Is Empty?

def is_empty(string):
    return not bool(string)
# fyi, from solution learned that since using the not keyword, string will automatically be interpreted in truthy/falsy context and don't need bool()


print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

'''


'''
# Is Empty or Blank?
def is_empty_or_blank(string):
    # Unnecessary. Just return not string.strip()
    return not string or not string.strip()


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
'''

# Capitalize Words
caps_this = 'launch school tech & talk'
capitalized = ' '.join([element.capitalize() for element in caps_this.split()])
print(capitalized)

# Check Prefix


def starts_with(string, prefix):
    return string.startswith(prefix)


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True


# Count Substrings
def count_substrings(string, substring):
    return string.count(substring)


print(count_substrings("lemon lemon lemon", "lemon"))  # 3
print(count_substrings("laLAlaLA", "la"))  # 2
print(count_substrings("launch", "uno"))  # 0
