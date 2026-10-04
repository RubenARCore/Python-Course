n = list(input())
result = ""

while len(n) > 0:
    biggest = 0
    index = 0

    for i in range(len(n)):
        if int(n[i]) > biggest:
            biggest = int(n[i])
            index = i

    result += str(biggest)
    n.pop(index)

print(result)