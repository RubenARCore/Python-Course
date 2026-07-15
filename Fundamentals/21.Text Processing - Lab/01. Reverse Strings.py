while True:
    data = input()
    if data == 'end':
        break

    print(f"{data} = {data[::-1]}")