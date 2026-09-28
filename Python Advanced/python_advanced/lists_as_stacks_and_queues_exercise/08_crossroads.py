from collections import deque


green_light = int(input())
free_window = int(input())

cars = deque()
total_cars = 0

while True:
    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{total_cars} total cars passed the crossroads.")
        break

    if command == "green":

        seconds = green_light

        while seconds > 0 and cars:

            car = cars.popleft()

            if len(car) <= seconds:
                seconds -= len(car)
                total_cars += 1

            else:
                passed = car[:seconds]
                remaining = car[seconds:]

                seconds = 0

                if len(remaining) <= free_window:
                    total_cars += 1
                    continue

                character_hit = remaining[free_window]

                print("A crash happened!")
                print(f"{car} was hit at {character_hit}.")
                exit()

    else:
        cars.append(command)