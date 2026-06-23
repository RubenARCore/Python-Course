data = list(map(int, input().split(", ")))
minimum_wealth = int(input())

if sum(data) / len(data) < minimum_wealth:
    print("No equal distribution possible")
    exit()

for i in range(0, len(data)):
    while data[i] < minimum_wealth:
        max_number = max(data)
        index = data.index(max_number)
        needed_number = minimum_wealth - data[i]
        data[index] -= needed_number
        data[i] += needed_number

print("["+", ".join(list(map(str, data))) + "]")


