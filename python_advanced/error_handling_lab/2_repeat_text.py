data = input()

try:
    n = int(input())
    print(n * data)
except ValueError:
    print("Variable times must be an integer")