contests = {}
users = {}

while True:
    data = input()

    if data == "no more time":
        break

    username, contest, points = data.split(" -> ")
    points = int(points)

    if contest not in contests:
        contests[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = points

        if username not in users:
            users[username] = 0

        users[username] += points

    else:
        old_points = contests[contest][username]

        if points > old_points:
            contests[contest][username] = points
            users[username] += points - old_points

for contest, participants in contests.items():
    print(f"{contest}: {len(participants)} participants")

    sorted_participants = sorted(
        participants.items(),
        key=lambda x: (-x[1], x[0])
    )

    for i, (username, points) in enumerate(sorted_participants, start=1):
        print(f"{i}. {username} <::> {points}")

print("Individual standings:")

sorted_users = sorted(
    users.items(),
    key=lambda x: (-x[1], x[0])
)

for i, (username, points) in enumerate(sorted_users, start=1):
    print(f"{i}. {username} -> {points}")