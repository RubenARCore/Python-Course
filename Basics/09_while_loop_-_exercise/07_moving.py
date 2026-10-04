a = int(input())
b = int(input())
c = int(input())

d = a * b * c

while d > 0:

    data = input()

    if data == 'Done':
        print(f'{d} Cubic meters left.')
        exit()

    data = int(data)
    d -= data

print(f'No more free space! You need {abs(d)} Cubic meters more.')