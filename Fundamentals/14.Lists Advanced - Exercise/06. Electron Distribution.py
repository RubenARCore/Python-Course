n = int(input())
result_ = []
counter = 1
while n > 0:
    capacity = 2 * (counter ** 2)
    if capacity < n:
        result_.append(capacity)
    else:
        result_.append(n)
    n -= capacity
    counter += 1
print("["+", ".join(map(str, result_))+"]")