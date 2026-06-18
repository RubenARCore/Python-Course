def data_type(data, n):
    if data == "int":
        return int(n) * 2
    elif data == "real":
        return f"{float(n) * 1.5:.2f}"
    elif data == "string":
        return f"${n}$"


data_ = input()
n = input()

print(data_type(data_, n))