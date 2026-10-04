budget = float(input())

total_sum = 0

while budget >= total_sum:
    data = input()
    if data == 'End':
        if budget >= total_sum:
            print(f'You bought everything needed.')
            exit(0)
    data = float(data)
    total_sum += data
    if budget < total_sum:
        print(f'You went in overdraft!')