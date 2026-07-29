n = int(input())
composes = {}

for i in range(n):
    data = input().split("|")

    piece = data[0]
    composer = data[1]
    key = data[2]

    composes[composer] = [piece, key]

while True:
    data = input()
    if data == "Stop":
        break

    data = data.split("|")



