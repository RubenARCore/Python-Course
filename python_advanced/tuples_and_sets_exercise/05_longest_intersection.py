n = int(input())
first_set = set()
second_set = set()
result = []
for _ in range(n):
    data = input().split("-")
    first_start = int(data[0].split(",")[0])
    first_end = int(data[0].split(",")[1])
    second_start = int(data[1].split(",")[0])
    second_end = int(data[1].split(",")[1])

    for i in range(first_start, first_end + 1):
        first_set.add(i)

    for i in range(second_start, second_end + 1):
        second_set.add(i)

    result.append(first_set.intersection(second_set))
    first_set.clear()
    second_set.clear()

max_length = max(result, key=len)

print(f"Longest intersection is [{', '.join(map(str, max_length))}] with length {len(max_length)}")
