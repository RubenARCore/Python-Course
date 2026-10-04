n = int(input())
sum_ = 0

for i in range(n):
    n = int(input())

    if sum_ + n > 255:
        print(f"Insufficient capacity!")
    else:
        sum_ += n


print(sum_)