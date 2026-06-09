n = int(input())
checker = False
for i in range(n):
    data = input()
    for char in data:
        if char == '.' or char == ',' or char == '_':
            # print(f'{data} is not pure!')
            checker = False
            break
        else:
            checker = True
    if checker:
        print(f"{data} is pure.")
    else:
        print(f"{data} is not pure!")
