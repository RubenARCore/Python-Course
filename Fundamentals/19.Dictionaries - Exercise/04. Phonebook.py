phone_book = {}
searches = 0

while True:
    data = input().split("-")

    if data[0].isdigit():
        searches = int(data[0])
        break

    phone_book[data[0]] = data[1]

for i in range(searches):
    data = input()
    if data in phone_book:
        print(f"{data} -> {phone_book[data]}")
    else:
        print(f"Contact {data} does not exist.")