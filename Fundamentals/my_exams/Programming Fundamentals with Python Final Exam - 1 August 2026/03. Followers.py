followers = {}

while True:
    data = input()
    if data == "Log out":
        break

    data = data.split(": ")
    command = data[0]

    if command == "New follower":
        username = data[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif command == "Like":
        username = data[1]
        count = int(data[2])
        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count
    elif command == "Comment":
        username = data[1]
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1
    elif command == "Blocked":
        username = data[1]
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

print(f"{len(followers)} followers")
for names in followers:
    total_sum = followers[names]["likes"] + followers[names]["comments"]
    print(f"{names}: {total_sum}")