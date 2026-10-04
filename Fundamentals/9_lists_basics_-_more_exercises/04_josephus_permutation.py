people = list(map(int, input().split()))
k = int(input())

result = []
index = 0

while people:
    index = (index + k - 1) % len(people)
    result.append(people.pop(index))
print('[', end='')
print(",".join(list(map(str, result))), end='')
print(']')