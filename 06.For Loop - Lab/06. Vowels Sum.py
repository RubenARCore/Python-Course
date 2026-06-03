input_text = input()

total_sum = 0

for char in input_text:
    if char in 'a':
        total_sum += 1
    elif char in 'e':
        total_sum += 2
    elif char in 'i':
        total_sum += 3
    elif char in 'o':
        total_sum += 4
    elif char in 'u':
        total_sum += 5

print(total_sum)