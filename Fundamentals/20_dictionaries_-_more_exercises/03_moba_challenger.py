players = {}

while True:
    command = input()

    if command == "Season end":
        break

    if " vs " in command:
        player1, player2 = command.split(" vs ")

        if player1 in players and player2 in players:

            common_position = False

            for position in players[player1]:
                if position in players[player2]:
                    common_position = True
                    break

            if common_position:
                player1_points = sum(players[player1].values())
                player2_points = sum(players[player2].values())

                if player1_points > player2_points:
                    del players[player2]

                elif player2_points > player1_points:
                    del players[player1]

        continue

    player, position, skill = command.split(" -> ")
    skill = int(skill)

    if player not in players:
        players[player] = {}

    if position not in players[player]:
        players[player][position] = skill

    else:
        if skill > players[player][position]:
            players[player][position] = skill


sorted_players = sorted(
    players.items(),
    key=lambda x: (-sum(x[1].values()), x[0])
)

for player, positions in sorted_players:

    total_skill = sum(positions.values())

    print(f"{player}: {total_skill} skill")

    sorted_positions = sorted(
        positions.items(),
        key=lambda x: (-x[1], x[0])
    )

    for position, skill in sorted_positions:
        print(f"- {position} <::> {skill}")