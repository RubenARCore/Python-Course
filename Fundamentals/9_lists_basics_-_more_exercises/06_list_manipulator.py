numbers = list(map(int, input().split()))

def is_even(x):
    return x % 2 == 0

def find_max_min(is_max, parity):
    filtered = []
    for i, n in enumerate(numbers):
        if parity == "even" and n % 2 == 0:
            filtered.append((n, i))
        elif parity == "odd" and n % 2 != 0:
            filtered.append((n, i))

    if not filtered:
        print("No matches")
        return

    if is_max:
        target = max(filtered, key=lambda x: x[0])[0]
    else:
        target = min(filtered, key=lambda x: x[0])[0]


    for n, i in reversed(filtered):
        if n == target:
            print(i)
            return


def first_last(count, parity, mode):
    if count > len(numbers):
        print("Invalid count")
        return

    result = []
    if parity == "even":
        arr = [x for x in numbers if x % 2 == 0]
    else:
        arr = [x for x in numbers if x % 2 != 0]

    if mode == "first":
        result = arr[:count]
    else:
        result = arr[-count:]

    print(result)


while True:
    command = input().split()

    if command[0] == "end":
        break

    if command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(numbers):
            print("Invalid index")
        else:
            numbers = numbers[index+1:] + numbers[:index+1]

    elif command[0] == "max":
        find_max_min(True, command[1])

    elif command[0] == "min":
        find_max_min(False, command[1])

    elif command[0] in ("first", "last"):
        count = int(command[1])
        parity = command[2]

        if count > len(numbers):
            print("Invalid count")
        else:
            first_last(count, parity, command[0])

print(numbers)