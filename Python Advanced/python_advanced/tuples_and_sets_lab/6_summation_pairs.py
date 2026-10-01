numbers = list(map(int, input().split()))
target = int(input())

seen = set()

for number in numbers:
    needed = target - number

    if needed in seen:
        print(f"{needed} + {number} = {target}")

    seen.add(number)