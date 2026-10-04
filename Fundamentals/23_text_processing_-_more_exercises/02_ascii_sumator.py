first = ord(input())
second = ord(input())
data = input()
total = 0
for char in data:
    if first < ord(char) < second:
        total += ord(char)
print(total)