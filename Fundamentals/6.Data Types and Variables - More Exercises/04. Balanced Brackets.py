n = int(input())

balance = 0
is_balanced = True

for _ in range(n):
    char = input()

    if char == '(':
        balance += 1
    elif char == ')':
        balance -= 1

    if balance < 0:
        is_balanced = False
        break

if balance != 0:
    is_balanced = False

print("BALANCED" if is_balanced else "UNBALANCED")