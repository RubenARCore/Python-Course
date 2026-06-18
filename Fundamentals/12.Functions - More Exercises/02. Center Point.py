result_list = []

for i in range(4):
    result_list.append(float(input()))
result_list.sort()

print(", ".join(map(str, result_list[:2])))