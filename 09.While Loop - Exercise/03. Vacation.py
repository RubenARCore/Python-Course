money_for_vacation = float(input())
existing_money = float(input())

days = 0
consecutive_spend = 0

while True:
    action = input()
    amount = float(input())

    days += 1

    if action == 'spend':
        consecutive_spend += 1
        existing_money -= amount

        if existing_money < 0:
            existing_money = 0

    else:
        consecutive_spend = 0
        existing_money += amount

    if consecutive_spend == 5:
        print("You can't save the money.")
        print(days)
        break

    if existing_money >= money_for_vacation:
        print(f'You saved the money for {days} days.')
        break