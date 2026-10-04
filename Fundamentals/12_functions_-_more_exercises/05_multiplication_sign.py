def check_numbers():
    lst = []
    negative_count = 0

    for i in range(3):
        lst.append(int(input()))

    for i in range(3):
        if lst[i] < 0:
            negative_count += 1

    if 0 in lst:
        print("zero")
    elif negative_count > 0:
        if negative_count == 2:
            print("positive")
        else:
            print("negative")
    else:
        print("positive")

check_numbers()