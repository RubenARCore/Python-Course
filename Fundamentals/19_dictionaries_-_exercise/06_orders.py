
order_list = {}

while True:
    data = input().split()
    if data[0] == "buy":
        break

    name, price, quantity = data

    if name not in order_list:
        order_list[name] = [float(price), int(quantity)]
    else:
        order_list[name][1] += int(quantity)
        order_list[name][0] = float(price)

for name, price in order_list.items():
    print(f"{name} -> {price[0] * price[1]:.2f}")

