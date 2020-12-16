import re

passwordRegex = re.compile(r'''(
    ^(?=.*[A-Z])                # at least one capital letters
    (?=.*[!@#$&*])                     # at least one of these special characters
    (?=.*[0-9])                 # at least one numeric digits
    (?=.*[a-z])          # at least one lower case letters
    .{8,}                              # at least 8 total digits
    $
    )''', re.VERBOSE)

 
def userInputPassCheck():
    mpass = input('enter your password: ')
    mo = passwordRegex.search(mpass)
    if not mo:
        print('your password is not strong,it must be 8 characters')
        return False
    else:
        print("Long and Strong, Good password")
        return True

userInputPassCheck()




