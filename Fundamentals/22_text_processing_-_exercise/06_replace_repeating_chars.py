data = list(input())
flag = False


for i in range(0, len(data)):
    if flag:
        break

    letter = data[i]
    if i == len(data) - 1:
        flag = True
        break
    while data[i] == data[i+1]:

        data.pop(i)

        if i == len(data)-1:
            flag = True
            break

print(''.join(data))