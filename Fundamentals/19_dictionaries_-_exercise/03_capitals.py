keys = input().split(", ")
values = input().split(", ")

result_dict = dict(zip(keys, values))

for key, value in result_dict.items():
    print(f"{key} -> {value}")