from functools import reduce

data = input().split()
result = []

for item in data:

    if item.lstrip("-").isdigit():
        result.append(int(item))
    else:
        if item == '-':
            temporary = reduce(lambda x, y: x - y, result)
            result.clear()
            result.append(temporary)
        elif item == '+':
           temporary = reduce(lambda x, y: x + y, result)
           result.clear()
           result.append(temporary)
        elif item == '*':
            temporary = reduce(lambda x, y: x * y, result)
            result.clear()
            result.append(temporary)
        elif item == '/':
            temporary = reduce(lambda x, y: x // y, result)
            result.clear()
            result.append(temporary)
print(*result)