length_of_sets = list(map(int, input().split()))

first_set = set()
second_set = set()

for _ in range(length_of_sets[0]):
    first_set.add(input())

for _ in range(length_of_sets[1]):
    second_set.add(input())

result = first_set.intersection(second_set)
print("\n".join(result))