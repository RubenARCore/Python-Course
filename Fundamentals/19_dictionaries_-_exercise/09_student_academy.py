n = int(input())

data_dict = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in data_dict:
        data_dict[name] = [grade]
    else:
        data_dict[name].append(grade)

for name, grades in data_dict.items():

    total = sum(grades) / len(grades)
    
    if total >= 4.5:
        print(f"{name} -> {total:.2f}")
