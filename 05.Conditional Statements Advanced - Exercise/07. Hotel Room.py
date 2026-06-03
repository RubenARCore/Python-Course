month = (input())
stay = int(input())

studios = 0
apartments = 0

if month == "May" or month == "October":
    if stay <= 7:
        studios += stay * 50
        apartments += stay * 65
    elif stay > 14:
        studios += stay * 50 * 0.7
        apartments += stay * 65 * 0.9
elif month == "June" or month == "September":
    if stay > 14:
        studios += 75.20 * stay * 0.8
        apartments += 68.7 * stay * 0.9
    else:
        studios += 75.20 * stay
        apartments += 68.7 * stay
else:
    if stay > 14:
        apartments += 77 * 0.9 * stay
        studios += 76 * stay
    else:
        apartments += 77 * stay * 0.9
        studios += 76 * stay

print(f'Apartment: {apartments:.2f} lv.')
print(f'Studio: {studios:.2f} lv.')