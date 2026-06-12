input_list = list(map(int, input().split(" ")))
n = int(input())
# control_list = input_list[:]
# removed_list = []
#
# input_list.sort()
#
#
# for i in range(n):
#     removed_list.append(input_list.pop(0))
#
# for i in range(len(removed_list)):
#     control_list.remove(removed_list[i])
#
# print(", ".join(map(str, control_list)))

for i in range(n):
    number = min(input_list)
    input_list.remove(number)

print(", ".join(map(str, input_list)))
