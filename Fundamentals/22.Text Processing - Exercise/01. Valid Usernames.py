data = input().split(", ")

for username in data:

    n = username.replace("-", "1").replace("_", "1")
    if 3 <= len(n) <= 16:
        if n.isalnum():
            print(username)