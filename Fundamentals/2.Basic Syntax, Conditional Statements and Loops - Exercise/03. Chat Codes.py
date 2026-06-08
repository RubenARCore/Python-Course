n = int(input())

for i in range(n):
    data = int(input())

    if data == 88:
        print("Hello")
    elif data == 86:
        print("How are you?")
    elif data < 88:
        print("GREAT!")
    else:
        print("Bye.")