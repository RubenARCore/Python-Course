n = int(input())

min_num = float('inf')
max_num = float('-inf')

for i in range(n):
    m = int(input())

    if m > max_num:
        max_num = m

    if m < min_num:
        min_num = m

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')