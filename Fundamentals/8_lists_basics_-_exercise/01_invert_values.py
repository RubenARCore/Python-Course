input_list = list(map(int, input().split()))


for i in range(0, len(input_list)):
    if input_list[i] < 0:
        input_list[i] *= -1
    else:
        input_list[i] -= input_list[i] * 2

print(input_list)