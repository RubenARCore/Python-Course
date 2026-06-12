cards = input().split()
shuffles = int(input())

for _ in range(shuffles):
    half = len(cards) // 2

    left = cards[:half]
    right = cards[half:]

    shuffled = []

    for i in range(half):
        shuffled.append(left[i])
        shuffled.append(right[i])

    cards = shuffled

print(cards)