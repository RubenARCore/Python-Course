max_number = float('inf')
data = ""
while data != 'Stop':
    data = input()
    if data == 'Stop':
        print(max_number)
        exit(0)
    data = int(data)

    if data < max_number:
        max_number = data
