n = int(input())
m = int(input())

n = n * m

while n > 0:
    data = input()

    if data == 'STOP':
        print(f'{n} pieces are left.')
        break

    data = int(data)
    n -= data

    if n < 0:
        print(f'No more cake left! You need {abs(n)} pieces more.')
