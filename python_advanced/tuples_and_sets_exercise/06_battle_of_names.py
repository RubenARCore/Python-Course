n = int(input())

even = set()
odd = set()

for i in range(1,n+1):
    summ = 0
    name = input()
    for char in name:
        summ += ord(char)
    summ //= i
    if summ % 2 == 0:
        even.add(summ)
    else:
        odd.add(summ)
if sum(even) == sum(odd):
    result = even.union(odd)
    print(", ".join(map(str, result)))
elif sum(odd) > sum(even):
    result = odd.difference(even)
    print(", ".join(map(str, result)))
elif sum(even) > sum(odd):
    result = odd.symmetric_difference(even)
    print(", ".join(map(str, result)))

