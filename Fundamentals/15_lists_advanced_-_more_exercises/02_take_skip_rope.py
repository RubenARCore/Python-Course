data = [char for char in input()]
# data = [char for char in "skipTest_String044160"]

number_lst, char_lst = [x for x in data if x.isdigit()], [x for x in data if not x.isdigit()]
result = []
take_list = []
skip_list = []

for i in range(0, len(number_lst)):
    if i % 2 == 0:
        take_list.append(number_lst[i])
    else:
        skip_list.append(number_lst[i])

for i in range(len(take_list)):
    for j in range(int(take_list[i])):
        if char_lst:
            result.append(char_lst[0])
            char_lst.pop(0)
    for j in range(int(skip_list[i])):
        if char_lst:
            char_lst.pop(0)

print("".join(result))