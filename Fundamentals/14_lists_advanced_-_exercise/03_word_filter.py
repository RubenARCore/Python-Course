data = input().split()

result = [x for x in data if len(x) % 2 == 0]

for i in result:
    print(i)