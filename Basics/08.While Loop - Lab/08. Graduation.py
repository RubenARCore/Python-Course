name = input()

grade_level = 1
failed_count = 0
total_sum = 0

while grade_level <= 12:
    grade = float(input())

    if grade < 4:
        failed_count += 1

        if failed_count > 1:
            print(f'{name} has been excluded at {grade_level} grade')
            break

        continue

    total_sum += grade
    grade_level += 1

else:
    print(f'{name} graduated. Average grade: {total_sum / 12:.2f}')