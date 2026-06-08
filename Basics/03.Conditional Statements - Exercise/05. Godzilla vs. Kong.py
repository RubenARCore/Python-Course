budget = float(input())
peoples = float(input())
clothes = float(input())

decor = budget * 0.1

money_for_clothes = clothes * peoples

if peoples >= 150:
    money_for_clothes = money_for_clothes - money_for_clothes * 0.1

total_sum = decor + money_for_clothes

if budget >= total_sum:
    print('Action!')
    print(f'Wingard starts filming with {budget-total_sum:.2f} leva left.')

else:
    print('Not enough money!')
    print(f'Wingard needs {total_sum - budget:.2f} leva more.')