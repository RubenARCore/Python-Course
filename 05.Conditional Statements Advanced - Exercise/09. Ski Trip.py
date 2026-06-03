days = int(input()) - 1
room_type = input()
rating = input()

total_sum = 0
discount = 0


if room_type == "room for one person":
    total_sum += days * 18
elif room_type == "apartment":
    if days < 10:
        total_sum += days * 25 * 0.7
    elif 10 <= days <= 15:
        total_sum += days * 25 * 0.65
    else:
        total_sum += days * 25 * 0.5
else:
    if days < 10:
        total_sum += days * 35 * 0.9
    elif 10 <= days <= 15:
        total_sum += days * 35 * 0.85
    else:
        total_sum += days * 35 * 0.8

if rating == "positive":
    total_sum *= 1.25
else:
    total_sum *= 0.9

print(f'{total_sum:.2f}')