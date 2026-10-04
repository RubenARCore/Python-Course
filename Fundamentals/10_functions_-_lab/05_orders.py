product_type = input()
n = int(input())

def calculate_product_price(type_, number):

    if type_ == "coffee":
        return number * 1.5
    elif type_ == "coke":
        return number * 1.40
    elif type_ == "water":
        return number * 1.00
    else:
        return number * 2.00

result = calculate_product_price(product_type, n)

print(f'{result:.2f}')