jury_count = int(input())

total_grades = 0
presentations = 0

while True:
    presentation = input()

    if presentation == "Finish":
        break

    presentation_sum = 0

    for _ in range(jury_count):
        grade = float(input())
        presentation_sum += grade

    average_grade = presentation_sum / jury_count

    print(f"{presentation} - {average_grade:.2f}.")

    total_grades += presentation_sum
    presentations += 1

final_assessment = total_grades / (presentations * jury_count)

print(f"Student's final assessment is {final_assessment:.2f}.")