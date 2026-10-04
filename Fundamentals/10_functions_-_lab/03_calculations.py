operator = input()
n = int(input())
m = int(input())

def calculator(operator, number1, number2):

    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        if number2 == 0:
            return "error"
        return int(number1 / number2)

result = calculator(operator, n, m)

print(result)