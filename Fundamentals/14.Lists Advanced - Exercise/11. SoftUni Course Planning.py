schedule = input().split(", ")

command = input()

while command != "course start":
    tokens = command.split(":")
    action = tokens[0]

    if action == "Add":
        lesson = tokens[1]
        if lesson not in schedule:
            schedule.append(lesson)

    elif action == "Insert":
        lesson = tokens[1]
        index = int(tokens[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif action == "Remove":
        lesson = tokens[1]
        if lesson in schedule:
            schedule.remove(lesson)
        exercise = f"{lesson}-Exercise"
        if exercise in schedule:
            schedule.remove(exercise)

    elif action == "Swap":
        lesson1 = tokens[1]
        lesson2 = tokens[2]

        if lesson1 in schedule and lesson2 in schedule:
            i1 = schedule.index(lesson1)
            i2 = schedule.index(lesson2)

            schedule[i1], schedule[i2] = schedule[i2], schedule[i1]

            ex1 = f"{lesson1}-Exercise"
            ex2 = f"{lesson2}-Exercise"

            if ex1 in schedule:
                schedule.remove(ex1)
                schedule.insert(schedule.index(lesson1) + 1, ex1)

            if ex2 in schedule:
                schedule.remove(ex2)
                schedule.insert(schedule.index(lesson2) + 1, ex2)

    elif action == "Exercise":
        lesson = tokens[1]
        exercise = f"{lesson}-Exercise"

        if lesson in schedule:
            if exercise not in schedule:
                idx = schedule.index(lesson)
                schedule.insert(idx + 1, exercise)
        else:
            schedule.append(lesson)
            schedule.append(exercise)

    command = input()

for i in range(len(schedule)):
    print(f"{i+1}.{schedule[i]}")