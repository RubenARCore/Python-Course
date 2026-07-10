contests = {}
submissions = {}

while True:
    data = input()
    if "end" in data:
        break

    data = data.split(":")
    contest = data[0]
    password = data[1]

    contests[contest] = password

while True:
    data = input()
    if "end" in data:
        break

    data = data.split("=>")
    contest = data[0]
    password = data[1]
    username = data[2]
    points = data[3]


