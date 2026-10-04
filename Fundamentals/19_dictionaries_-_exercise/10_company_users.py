company_users = {}

while True:
    data = input()
    if data == "End":
        break
    data = data.split(" -> ")

    if data[0] not in company_users:
        company_users[data[0]] = [data[1]]
    else:
        if data[1] not in company_users[data[0]]:
            company_users[data[0]].append(data[1])

for company, names in company_users.items():
    print(f"{company}")
    for name in names:
        print(f"-- {name}")