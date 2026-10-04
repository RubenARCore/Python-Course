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