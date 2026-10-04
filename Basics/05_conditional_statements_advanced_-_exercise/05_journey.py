budget = float(input())
season = input()

total_sum = 0
location = ""
type_of_location = ""

if budget <= 100:
    if season == 'summer':
        total_sum += budget * 0.3
        location = 'Bulgaria'
        type_of_location = 'Camp'
    else:
        total_sum += budget * 0.7
        location = 'Bulgaria'
        type_of_location = 'Hotel'
elif budget <= 1000:
    if season == 'summer':
        total_sum += budget * 0.4
        location = 'Balkans'
        type_of_location = 'Camp'
    else:
        total_sum += budget * 0.8
        location = 'Balkans'
        type_of_location = 'Hotel'
elif budget > 1000:
        total_sum += budget * 0.9
        location = 'Europe'
        type_of_location = 'Hotel'

print(f'Somewhere in {location}')
print(f'{type_of_location} - {total_sum:.2f}')