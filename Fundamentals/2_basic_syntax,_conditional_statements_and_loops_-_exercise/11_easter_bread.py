budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price = flour_price * 1.25

bread_cost = flour_price + egg_price + (milk_price * 0.25)

loaves = 0
eggs = 0

while budget >= bread_cost:
    budget -= bread_cost
    loaves += 1
    eggs += 3

    if loaves % 3 == 0:
        eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")