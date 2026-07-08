students = {}
course = None



while True:
    data = input().split(":")
    if len(data) == 1:
        course = data[0].replace("_", " ")
        break

    name = data[0]
    student_id = int(data[1])
    course_name = data[2]

    if course_name not in students:
        students[course_name] = {}

    students[course_name][name] = student_id

for student in students[course]:
    print(f"{student} - {students[course][student]}")


