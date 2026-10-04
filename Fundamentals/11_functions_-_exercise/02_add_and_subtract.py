def sum_numbers(first, second):
    return first + second


def subtract(sum_result, third):
    return sum_result - third


def add_and_subtract(first, second, third):
    total = sum_numbers(first, second)
    return subtract(total, third)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))