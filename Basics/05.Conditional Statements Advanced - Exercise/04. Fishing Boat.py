budget = float(input())
season = input()
fisherman = int(input())

total_sum = 0

if season == 'Spring':
    if fisherman <= 6:
        total_sum += 3000 * 0.9
    elif 7 < fisherman <= 11:
        total_sum += 3000 * 0.85
    else:
        total_sum += 3000 * 0.75
elif season == 'Summer' or season == 'Autumn':
    if fisherman <= 6:
        total_sum += 4200 * 0.9
    elif 7 < fisherman <= 11:
        total_sum += 4200 * 0.85
    else:
        total_sum += 4200 * 0.75
else:
    if fisherman <= 6:
        total_sum += 2600 * 0.9
    elif 7 < fisherman <= 11:
        total_sum += 2600 * 0.85
    else:
        total_sum += 2600 * 0.75

if fisherman % 2 == 0 and season != 'Autumn':
    total_sum *= 0.95


if total_sum - budget <= 0:
    print(f'Yes! You have {budget - total_sum:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_sum - budget:.2f} leva.')