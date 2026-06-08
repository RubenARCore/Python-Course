n = float(input())

if n == 0:
    print("0")
elif n < 0:
    if -1 <= n < 0:
        print("small negative")
    elif -1000000 <= n <= -1:
        print("negative")
    else:
        print("large negative")
else:
    if 0 < n <= 1:
        print('small positive')
    elif 1 < n < 1000000:
        print('positive')
    else:
        print('large positive')