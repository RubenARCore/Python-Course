expression = input()

stack = []

for index, char in enumerate(expression):
    if char == '(':
        stack.append(index)

    elif char == ')':
        start = stack.pop()
        print(expression[start:index + 1])