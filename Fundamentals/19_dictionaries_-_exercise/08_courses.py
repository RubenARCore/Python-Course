courses = {}

while True:
    data = input().split(" : ")

    if data[0] == "end":
        break

    if data[0] not in courses:
        courses[data[0]] = [data[1]]
    else:
        courses[data[0]].append(data[1])


for name_of_course, course in courses.items():
    print(f"{name_of_course}: {len(course)}")
    for name in course:
        print(f"-- {name}")
