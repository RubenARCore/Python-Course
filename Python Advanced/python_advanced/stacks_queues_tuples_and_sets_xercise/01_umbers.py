first_set = set(input().split())
second_set = set(input().split())
n = int(input())
checker = False
for _ in range(n):
    data = input().split(" ", 2)

    if data[0] == "Add":
        if data[1] == "First":
            first_set.update(data[2].split())
        else:
            second_set.update(data[2].split())
    elif data[0] == "Remove":
        if data[1] == "First":
            for item in data[2].split():
                first_set.discard(item)
        else:
            for item in data[2].split():
                second_set.discard(item)
    elif data[0] == "Check":
        checker = first_set.issubset(second_set) or second_set.issubset(first_set)
        print(checker)

print(*sorted(map(int, first_set)), sep=", ")
print(*sorted(map(int, second_set)), sep=", ")
