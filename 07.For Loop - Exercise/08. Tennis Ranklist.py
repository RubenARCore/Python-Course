n = int(input())
starting_points = int(input())

average_sum = 0
win_count = 0

for i in range(n):
    tournament_type = input()
    if tournament_type == 'W':
        starting_points += 2000
        average_sum += 2000
        win_count += 1
    elif tournament_type == 'F':
        starting_points += 1200
        average_sum += 1200
    else:
        starting_points += 720
        average_sum += 720

print(f'Final points: {starting_points}')
print(f'Average points: {int(average_sum / n)}')
print(f'{win_count/n * 100:.2f}%')