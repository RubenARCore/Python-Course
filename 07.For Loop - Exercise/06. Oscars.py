name = input()
points = float(input())
n = int(input())

is_nominated = False

for i in range(n):
    m = input()
    p = float(input())

    points += (len(m) * p) / 2

    if points > 1250.5:
        is_nominated = True
        break

if is_nominated:
    print(f'Congratulations, {name} got a nominee for leading role with {points:.1f}!')
else:
    print(f'Sorry, {name} you need {1250.5 - points:.1f} more!')