data = input().split()

products = {}

while data[0] != "statistics":

    key = data[0]
    value = int(data[1])

    if not key in products:
        products[key] = value
    else:
        products[key] += value

    data = input().split()

print("Products in stock:")
for key, value in products.items():
    print(f"- {key} {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")