student = 0
standard = 0
kid = 0
total_tickets = 0

while True:
    movie = input()

    if movie == "Finish":
        break

    free_seats = int(input())
    sold = 0

    while sold < free_seats:
        ticket = input()

        if ticket == "End":
            break

        total_tickets += 1
        sold += 1

        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1

    percent_full = (sold / free_seats) * 100
    print(f"{movie} - {percent_full:.2f}% full.")

# финални проценти
print(f"Total tickets: {total_tickets}")
print(f"{(student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / total_tickets) * 100:.2f}% kids tickets.")