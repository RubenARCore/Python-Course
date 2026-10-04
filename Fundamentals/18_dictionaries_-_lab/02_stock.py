data = input().split()
products_to_search = input().split()
stock = {}

for i in range(0,len(data), 2):
    key = data[i]
    value = data[i+1]
    stock[key] = value

for product in products_to_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")