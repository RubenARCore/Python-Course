data = input().split(", ")
result_dict = {}
for item in data:
    result_dict[item] = ord(item)

print(result_dict)