type = input()
rows = int(input())
columns = int(input())

total_sum = 0

if type == 'Premiere':
    total_sum = rows * columns * 12
    print(f'{total_sum:.2f} leva')
elif type == 'Normal':
    total_sum = rows * columns * 7.5
    print(f'{total_sum:.2f} leva')
else:
    total_sum = rows * columns * 5
    print(f'{total_sum:.2f} leva')