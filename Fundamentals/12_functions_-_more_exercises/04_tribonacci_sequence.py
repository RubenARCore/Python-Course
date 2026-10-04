n = int(input())

def tribonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    seq = [1, 1, 2]

    for _ in range(n - 3):
        seq.append(seq[-1] + seq[-2] + seq[-3])

    return seq

print(" ".join(map(str, tribonacci(n))))