city = input()
money = float(input())

if money < 0:
    print('error')
elif city == 'Sofia':
    if 0 <= money <= 500:
        print(f'{money * 0.05:.2f}')
    elif 500 < money <= 1000:
        print(f'{money * 0.07:.2f}')
    elif 1000 < money <= 1500:
        print(f'{money * 0.08:.2f}')
    else:
        print(f'{money * 0.12:.2f}')
elif city == 'Varna':
    if 0 <= money <= 500:
        print(f'{money * 0.045:.2f}')
    elif 500 < money <= 1000:
        print(f'{money * 0.075:.2f}')
    elif 1000 < money <= 1500:
        print(f'{money * 0.10:.2f}')
    else:
        print(f'{money * 0.13:.2f}')
elif city == 'Plovdiv':
    if 0 <= money <= 500:
        print(f'{money * 0.055:.2f}')
    elif 500 < money <= 1000:
        print(f'{money * 0.08:.2f}')
    elif 1000 < money <= 1500:
        print(f'{money * 0.12:.2f}')
    else:
        print(f'{money * 0.145:.2f}')
else:
    print('error')