items_input = input().split("|")
budget = float(input())

max_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

bought_prices = []
profit = 0

for item in items_input:
    item_type, price = item.split("->")
    price = float(price)

    if price > max_prices[item_type]:
        continue

    if budget < price:
        continue

    budget -= price
    bought_prices.append(price)

selling_prices = []
for price in bought_prices:
    new_price = price * 1.40
    selling_prices.append(new_price)
    profit += new_price - price
    budget += new_price

print(" ".join(f"{p:.2f}" for p in selling_prices))
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")