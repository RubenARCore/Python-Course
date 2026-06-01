nylon = float(input())+2
paint = float(input())
thinner = float(input())
hours = float(input())

nylon = nylon * 1.5
paint = (paint + (paint * 0.1)) * 14.5
thinner = thinner * 5

sum = nylon + paint + thinner + 0.4

master_money = sum * 0.3 * hours

print(master_money + sum)