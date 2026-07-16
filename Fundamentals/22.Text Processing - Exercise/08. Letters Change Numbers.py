data = input().split()
result = 0
total_result = 0
letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

for string in data:

    number = int(''.join(ch for ch in string if ch.isdigit()))
    if string[0].isupper():
        position = letters.index(string[0].lower()) + 1
        result = number / position
    elif string[0].islower():
        position = letters.index(string[0].lower()) + 1
        result = number * position

    if string[-1].isupper():
        position = letters.index(string[-1].lower()) + 1
        result -= position
    elif string[-1].islower():
        position = letters.index(string[-1].lower()) + 1
        result += position

    total_result += result

print(f"{total_result:.2f}")