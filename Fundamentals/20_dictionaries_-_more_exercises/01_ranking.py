contests = {}
submissions = {}

while True:
    data = input()
    if data == "end of contests":
        break

    contest, password = data.split(":")
    contests[contest] = password

while True:
    data = input()
    if data == "end of submissions":
        break

    contest, password, username, points = data.split("=>")
    points = int(points)

    if contest in contests and contests[contest] == password:

        if username not in submissions:
            submissions[username] = {}

        if contest not in submissions[username]:
            submissions[username][contest] = points
        elif points > submissions[username][contest]:
            submissions[username][contest] = points

best_candidate = max(
    submissions,
    key=lambda user: sum(submissions[user].values())
)

best_points = sum(submissions[best_candidate].values())

print(
    f"Best candidate is {best_candidate} "
    f"with total {best_points} points."
)

print("Ranking:")

for username in sorted(submissions):
    print(username)

    for contest, points in sorted(
        submissions[username].items(),
        key=lambda x: -x[1]
    ):
        print(f"#  {contest} -> {points}")