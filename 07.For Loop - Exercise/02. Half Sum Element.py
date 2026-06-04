n = int(input())

total_sum = 0
max_num = float('-inf')

for i in range(n):
    num = int(input())
    total_sum += num

    if num > max_num:
        max_num = num

other_sum = total_sum - max_num

if max_num == other_sum:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs(max_num - other_sum)}")