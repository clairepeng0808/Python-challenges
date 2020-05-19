# At least 8 char long
# Contain any sort of letters,numbers,$%#@

import re
pattern = re.compile(r"[\w$%#@]{8,}")

print('\n\nYour password needs to be at least 8 char long, numbers, letters, and $,#,%,@ are accepted.')

while True:
    password = input('\nPlease set up your password: ')

    if pattern.fullmatch(password) == None:
        print('Incorrect password format.')

    else:
        print('Your password has been setup successfully.')
        break
