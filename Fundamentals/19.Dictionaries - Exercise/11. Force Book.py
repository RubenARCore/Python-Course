import re
force_book = {}
while True:
    data = input()
    if data == "Lumpawaroo":
        break

    force_side, delimiter, force_user = re.split(r"\s*(\||->)\s*", data)

    if delimiter == "->":
        force_side, force_user = force_user, force_side

        old_side = None

        for side, users in force_book.items():
            if force_user in users:
                old_side = side
                break

        if old_side:
            force_book[old_side].remove(force_user)

        if force_side not in force_book:
            force_book[force_side] = []

        force_book[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    else:

        user_exists = False

        for users in force_book.values():
            if force_user in users:
                user_exists = True
                break

        if user_exists:
            continue

        if force_side not in force_book:
            force_book[force_side] = []

        force_book[force_side].append(force_user)

for side, users in force_book.items():

    if users:
        print(f"Side: {side}, Members: {len(users)}")

        for user in users:
            print(f"! {user}")