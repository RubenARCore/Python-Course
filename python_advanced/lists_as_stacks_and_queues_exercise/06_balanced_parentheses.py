data = list(input())

brackets = {
    ')': '(',
    ']': '[',
    '}': '{'
}

stack = []

for char in data:

    if char in "([{":
        stack.append(char)

    else:
        if not stack or stack[-1] != brackets[char]:
            print("NO")
            break

        stack.pop()

else:
    if not stack:
        print("YES")
    else:
        print("NO")