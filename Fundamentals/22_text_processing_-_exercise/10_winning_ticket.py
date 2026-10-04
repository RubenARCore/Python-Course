tickets = [ticket.strip() for ticket in input().split(",")]

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left = ticket[:10]
    right = ticket[10:]
    found = False

    for symbol in "@#$^":
        for count in range(10, 5, -1):
            sequence = symbol * count

            if sequence in left and sequence in right:
                if count == 10:
                    print(f'ticket "{ticket}" - {count}{symbol} Jackpot!')
                else:
                    print(f'ticket "{ticket}" - {count}{symbol}')

                found = True
                break

        if found:
            break

    if not found:
        print(f'ticket "{ticket}" - no match')