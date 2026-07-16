data = input().split()

for char in data:
    print(f"{char * len(char)}", end="")