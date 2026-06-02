input_number = int(input())
result_number = input_number
bonus = 0

if input_number < 100:
    input_number += 5
    bonus += 5
elif input_number <= 1000:
    bonus += input_number * 0.2
    input_number += input_number * 0.2
else:
    bonus += input_number * 0.1
    input_number += input_number * 0.1

if result_number % 2 == 0:
    input_number += 1
    bonus += 1
elif result_number % 10 == 5:
    input_number += 2
    bonus += 2

print(bonus)
print(input_number)
