total_steps = 0

while True:
    steps = input()


    if steps == "Going home":
        last_steps = int(input())
        if total_steps + last_steps >= 10000:
            print(f'Goal reached! Good job!')
            print(f'{(total_steps + last_steps) - 10000} steps over the goal!')
            break
        else:
            print(f'{10000 - (total_steps + last_steps)} more steps to reach goal.')
            break

    steps = int(steps)
    total_steps += steps

    if total_steps >= 10000:
        print(f'Goal reached! Good job!')
        print(f'{total_steps - 10000} steps over the goal!')
        break
