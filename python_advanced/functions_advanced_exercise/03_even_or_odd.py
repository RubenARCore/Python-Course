def even_odd(*args):
    even = []
    odd = []
    command = args[-1]

    for i in range(len(args)-1):
        if args[i] % 2 == 0:
            even.append(args[i])
        else:
            odd.append(args[i])

    if command == 'even':
        return even
    elif command == 'odd':
        return odd


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))