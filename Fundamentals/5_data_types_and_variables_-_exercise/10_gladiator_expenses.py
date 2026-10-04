lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_breaks = 0
sword_breaks = 0
shield_breaks = 0
armor_breaks = 0

for fight in range(1, lost_fights + 1):

    helmet_broken = False
    sword_broken = False

    if fight % 2 == 0:
        helmet_breaks += 1
        helmet_broken = True

    if fight % 3 == 0:
        sword_breaks += 1
        sword_broken = True

    if helmet_broken and sword_broken:
        shield_breaks += 1

        if shield_breaks % 2 == 0:
            armor_breaks += 1

expenses = (
    helmet_breaks * helmet_price +
    sword_breaks * sword_price +
    shield_breaks * shield_price +
    armor_breaks * armor_price
)

print(f"Gladiator expenses: {expenses:.2f} aureus")