n = int(input())
query = []

for _ in range(n):
    data = input().split()

    if data[0] == "1":
        query.append(int(data[1]))
    elif data[0] == "2":
        if len(query) == 0:
            continue
        query.pop()
    elif data[0] == "3":
        if len(query) == 0:
            continue
        print(max(query))
    elif data[0] == "4":
        if len(query) == 0:
            continue
        print(min(query))
result = [str(x) for x in query]
result.reverse()
print(", ".join(result))
