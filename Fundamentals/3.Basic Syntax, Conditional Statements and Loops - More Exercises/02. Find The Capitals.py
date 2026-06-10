data = input()
counter = 0
print(f'[', end='')
for i, char in enumerate(data):
    if i == len(data) - 1:
        print(i, end='')
        break
    elif char.isupper():
        print(f'{i}', end=', ')


print(']')


