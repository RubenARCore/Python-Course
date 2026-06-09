n = input()

while n != "End":
    if n == "SoftUni":
        n = input()
        continue

    for char in n:
        print(f'{char}{char}', end='')

    print()
    n = input()