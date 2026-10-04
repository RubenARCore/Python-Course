total_sum = 0


while True:
    destination =input()
    if destination == 'End':
        exit()
    budget = float(input())


    while True:
        money = float(input())
        total_sum += money
        if total_sum >= budget:
            print(f'Going to {destination}!')
            total_sum = 0
            budget = 0
            break
