n = int(input())

is_balanced = True
open_bracket = False

for _ in range(n):
    line = input()

    if line == '(':
        if open_bracket:
            is_balanced = False
            break
        open_bracket = True

    elif line == ')':
        if not open_bracket:
            is_balanced = False
            break
        open_bracket = False

if open_bracket:
    is_balanced = False

print("BALANCED" if is_balanced else "UNBALANCED")