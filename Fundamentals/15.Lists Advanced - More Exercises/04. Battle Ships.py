n = int(input())
field = []

for _ in range(n):
    field.append(list(map(int, input().split())))

attacks = input().split()
destroyed_ships = 0

for attack in attacks:
    r_str, c_str = attack.split('-')
    row, col = int(r_str), int(c_str)

    if field[row][col] > 0:
        field[row][col] -= 1

        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)