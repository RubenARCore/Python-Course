n = list(map(int, input().split(", ")))
counter = 0


# for i in range(len(n)):
#     if 0 in n:
#         n.remove(0)
#         counter += 1
#
# for i in range(counter):
#     n.append(0)
#
# print(n)

while 0 in n:
    n.remove(0)
    counter += 1

for i in range(counter):
     n.append(0)

print(n)
