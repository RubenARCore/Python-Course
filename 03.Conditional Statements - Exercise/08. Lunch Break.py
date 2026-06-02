import math

name = input()
movie_time = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
rest_time = break_time * 0.25

free_time = break_time - lunch_time - rest_time

if free_time >= movie_time:
    print(
        f'You have enough time to watch {name} and '
        f'left with {math.ceil(free_time - movie_time)} minutes free time.'
    )
else:
    print(
        f'You don\'t have enough time to watch {name}, '
        f'you need {math.ceil(movie_time - free_time)} more minutes.'
    )