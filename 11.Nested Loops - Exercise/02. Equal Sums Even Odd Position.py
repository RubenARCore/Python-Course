start = int(input())
end = int(input())

for num in range(start, end + 1):
    even_sum = 0
    odd_sum = 0

    digits = str(num)

    for i in range(6):
        digit = int(digits[i])

        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    if even_sum == odd_sum:
        print(num, end=" ")