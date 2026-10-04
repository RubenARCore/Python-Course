data = input().lower().split()
dict_ = {}

for word in data:
    if word not in dict_:
        dict_[word] = 1
    else:
        dict_[word] += 1

for key, value in dict_.items():
    if value % 2 != 0:
        print(f"{key}", end=" ")
