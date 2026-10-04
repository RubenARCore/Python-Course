flowers_type = input()
count_flowers = int(input())
budget = float(input())

total_sum = 0

if flowers_type == 'Roses':
    if count_flowers > 80:
        total_sum += count_flowers * 5 * 0.9
    else:
        total_sum += count_flowers * 5
elif flowers_type == 'Dahlias':
    if count_flowers > 90:
        total_sum += count_flowers * 3.8 * 0.85
    else:
        total_sum += count_flowers * 3.8
elif flowers_type == 'Tulips':
    if count_flowers > 80:
        total_sum += count_flowers * 2.8 * 0.85
    else:
        total_sum += count_flowers * 2.8
elif flowers_type == 'Narcissus':
    if count_flowers < 120:
        total_sum += count_flowers * 3 * 1.15
    else:
        total_sum += count_flowers * 3
elif flowers_type == 'Gladiolus':
    if count_flowers < 80:
        total_sum += count_flowers * 2.5 * 1.2
    else:
        total_sum += count_flowers * 2.5

if budget >= total_sum:
    print(f'Hey, you have a great garden with {count_flowers} {flowers_type} and {budget - total_sum:.2f} leva left.')
else:
    print(f'Not enough money, you need {total_sum - budget:.2f} leva more.')