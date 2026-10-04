def loading_bar(n):
    n = n // 10

    if n == 10:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{n * 10}% [", end="")
        for i in range(n):
            print("%", end="")
        for j in range(10 - n):
            print(".", end="")
        print("]")
        print("Still loading...")


n = int(input())
loading_bar(n)