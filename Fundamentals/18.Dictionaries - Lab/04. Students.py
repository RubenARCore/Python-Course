data_lst = []
students = {}

while True:
    data = input().split(":", 2)
    if len(data) == 1:
        break
    data_lst.append(data)
    students[data[0]] = int(data[1])