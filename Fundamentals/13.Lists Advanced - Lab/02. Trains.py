n = [0] * int(input())

while True:
    data = input().split()
    if data[0] == "add":
        n[-1] += int(data[1])
    elif data[0] == "insert":
        n[int(data[1])] += int(data[2])
    elif data[0] == "leave":
        n[int(data[1])] -= int(data[2])
    elif data[0] == "End":
        print("["+", ".join(map(str,n)) + "]")
        exit()