from itertools import count

age = int(input())
washing_machine = float(input())
price_per_toy = int(input())

toys = 0
money = 0
count = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        count += 1
        money += count * 10
    else:
        toys += 1

total_money = money - count + toys * price_per_toy

if total_money >= washing_machine:
    print(f'Yes! {total_money - washing_machine:.2f}')
else:
    print(f'No! {washing_machine - total_money:.2f}')