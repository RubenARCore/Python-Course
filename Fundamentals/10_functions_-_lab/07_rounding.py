n = list(map(float, input().split()))
m = []
def rounding_ (number):

    for i in range(len(number)):
      m.append(round(number[i]))

rounding_(n)

print(f"[{', '.join(map(str, m))}]")

