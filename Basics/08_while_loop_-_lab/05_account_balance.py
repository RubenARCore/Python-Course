total_sum = 0

while True:
    income = input()

    if income == 'NoMoreMoney':
        print(f'Total: {total_sum}')
        break

    income = float(income)

    if income < 0:
        print('Invalid operation!')
        print(f'Total: {total_sum}')
        break

    total_sum += income
    print(f'Increase: {income:.2f}')