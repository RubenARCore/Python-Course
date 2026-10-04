import numbers
password = list(input())
flag = True

if not 6 <= len(password) <= 10:
    print(f'Password must be between 6 and 10 characters')
    flag = False

def digits_checker (chars):
    counter_digits = 0
    for char in chars:

        if char.isdigit():
            counter_digits += 1
        else:
            counter_digits = 0

        if counter_digits == 2:
            break

    if 2 > counter_digits:
        return True
    else:
        return False

def letters_digits_checker(chars):
    flag_ = True
    for char in chars:
        if not char.isalnum():
            flag_ = False
            break
    return flag_

if not letters_digits_checker(password):
    print('Password must consist only of letters and digits')
    flag = False

if digits_checker(password):
    print('Password must have at least 2 digits')
    flag = False

if flag:
    print('Password is valid')