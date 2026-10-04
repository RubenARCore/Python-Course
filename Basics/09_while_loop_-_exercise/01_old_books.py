book = input()

counter = 0
data = ""

while data != "No More Books":
    data = input()
    if data == book:
        print(f'You checked {counter} books and found it.')
        exit(0)
    if data == "No More Books":
        print(f'The book you search is not here!')
        print(f'You checked {counter} books.')
    counter += 1