import math

n = int(input())
salary = float(input())

for i in range(1, n + 1):

    m = input()
    if m == 'Facebook':
        salary -= 150
    elif m == 'Instagram':
        salary -= 100
    elif m == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        exit()

print(f'{math.trunc(salary)}')