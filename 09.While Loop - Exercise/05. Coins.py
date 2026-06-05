change = float(input())

coins = 0
amount = round(change * 100)

coin_values = [200, 100, 50, 20, 10, 5, 2, 1]

for coin in coin_values:
    coins += amount // coin
    amount %= coin

print(coins)