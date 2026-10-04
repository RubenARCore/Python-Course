n = list(map(float, input().split(" ")))
m = []


def absolute_value(number):

    for i in range(len(number)):
        m.append(abs(number[i]))

absolute_value(n)

print(f"[{', '.join(map(str, m))}]")