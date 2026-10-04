product = input()
city = input()
quantity = float(input())

total_sum = 0

if city == 'Sofia':
    if product == 'coffee':
        total_sum += quantity * 0.5
    elif product == 'water':
        total_sum += quantity * 0.8
    elif product == 'beer':
        total_sum += quantity * 1.2
    elif product == 'sweets':
        total_sum += quantity * 1.45
    elif product == 'peanuts':
        total_sum += quantity * 1.6
elif city == 'Plovdiv':
    if product == 'coffee':
        total_sum += quantity * 0.4
    elif product == 'water':
        total_sum += quantity * 0.7
    elif product == 'beer':
        total_sum += quantity * 1.15
    elif product == 'sweets':
        total_sum += quantity * 1.3
    elif product == 'peanuts':
        total_sum += quantity * 1.5
elif city == 'Varna':
    if product == 'coffee':
        total_sum += quantity * 0.45
    elif product == 'water':
        total_sum += quantity * 0.7
    elif product == 'beer':
        total_sum += quantity * 1.1
    elif product == 'sweets':
        total_sum += quantity * 1.35
    elif product == 'peanuts':
        total_sum += quantity * 1.55

print(f'{total_sum:.2f}')