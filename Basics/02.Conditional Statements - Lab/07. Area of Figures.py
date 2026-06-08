import math

shape = input()
first_number = float(input())

if shape == 'square':
    print(f'{first_number * first_number:.3f}')
elif shape == 'rectangle':
    second_number = float(input())
    print(f'{first_number * second_number:.3f}')
elif shape == 'circle':
    print(f'{math.pi * first_number * first_number:.3f}')
else:
    second_number = float(input())
    print(f'{(first_number * second_number) / 2:.3f}')
