n = int(input())
data = 0

while data <= n:
    data += int(input())
    if data >= n:
        print(data)
        exit()
