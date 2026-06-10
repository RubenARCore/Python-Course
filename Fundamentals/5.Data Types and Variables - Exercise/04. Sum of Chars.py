n = int(input())
sum_ = 0
for i in range(1, n + 1):
    n = input()
    sum_ += ord(n)

print(f'The sum equals: {sum_}')