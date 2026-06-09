n = int(input())

total_price = 0.0

for i in range(1, n + 1):
    price_per_capsule = float(input())
    days = float(input())
    capsule_per_day = float(input())

    price = 0.0

    if 0.01 <= price_per_capsule <= 100.00 and 1 <= days <= 31 and 1 <= capsule_per_day <= 2000:
        price = price_per_capsule * days * capsule_per_day
        total_price += price
        print(f'The price for the coffee is: ${price:.2f}')


print(f'Total: ${total_price:.2f}')