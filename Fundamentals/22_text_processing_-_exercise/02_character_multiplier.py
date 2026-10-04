data = input().split()
result = 0
smaller = ""
bigger = ""

if len(data[0]) < len(data[1]):
    smaller = data[0]
    bigger = data[1]
else:
    smaller = data[1]
    bigger = data[0]

for i in range(0, len(smaller)):

    result += ord(data[0][i]) * ord(data[1][i])

    if i == len(smaller)-1:

        for j in range(i+1, len(bigger)):
            result += ord(bigger[j])


print(result)