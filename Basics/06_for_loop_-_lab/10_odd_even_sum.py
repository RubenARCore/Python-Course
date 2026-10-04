n = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    m = int(input())
    if i % 2 == 0:
        even_sum += m
    else:
        odd_sum += m

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum - odd_sum)}')