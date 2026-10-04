data = list(map(int, input().split(", ")))


positives = [x for x in data if x >= 0]
negatives = [x for x in data if x < 0]
evens = [x for x in data if x % 2 == 0]
odds = [x for x in data if x % 2 != 0]



print(f'Positive: {", ".join(list(map(str, positives)))}')
print(f'Negative: {", ".join(list(map(str, negatives)))}')
print(f'Even: {", ".join(list(map(str, evens)))}')
print(f'Odd: {", ".join(list(map(str, odds)))}')


