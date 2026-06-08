n = float(input())

if n == 0:
    print("0")
elif n < 0:
    if -1 <= n < 0:
        print("small negative")
    else:
        print("negative")