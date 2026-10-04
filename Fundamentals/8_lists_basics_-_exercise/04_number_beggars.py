offers = list(map(int, input().split(", ")))
beggars = int(input())

result = []

for beggar in range(beggars):
    current_sum = 0

    for index in range(beggar, len(offers), beggars):
        current_sum += offers[index]

    result.append(current_sum)

print(result)