n = list(map(str, input().split(", ")))
m = list(map(str, input().split(", ")))
lst = []

for i in n:
    for j in m:
        if i in j:
            lst.append(i)
            break

print(lst)
