n = int(input())
checker = True
for i in range(n):
    data = input()
    for char in data:
        if char == '.' or char == ',' or char == '_':
            # print(f'{data} is not pure!')
            checker = True
            break
        else:
            checker = False
