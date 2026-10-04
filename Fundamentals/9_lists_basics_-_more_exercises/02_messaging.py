number = list(map(int, input().split()))
chars = list(input())

for i in range(len(number)):
    control_number = number[i]
    sum_digits = 0

    while control_number > 0:
        sum_digits += control_number % 10
        control_number //= 10

    index = sum_digits % len(chars)

    print(chars.pop(index), end="")