input_list = input().split(" ")

counter_a = 11
counter_b = 11
team_a_players = []
team_b_players = []

for i in range(len(input_list)):
    control_list = input_list[i].split("-")
    if control_list[0] == "A":
        if control_list[1] in team_a_players:
            continue
        counter_a -= 1
        team_a_players.append(control_list[1])
    elif control_list[0] == "B":
        if control_list[1] in team_b_players:
            continue
        counter_b -= 1
        team_b_players.append(control_list[1])

    if counter_a < 7:
        print(f'Team A - {counter_a}; Team B - {counter_b}')
        print(f'Game was terminated')
        break
    elif counter_b < 7:
        print(f'Team A - {counter_a}; Team B - {counter_b}')
        print(f'Game was terminated')
        break
