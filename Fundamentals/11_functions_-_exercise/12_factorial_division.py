n = int(input())
m = int(input())

def factorial_division(n_, m_):
    first_factorial = 1
    second_factorial = 1

    for i in range(n_, 0, -1):
        first_factorial *= i

    for j in range(m_, 0, -1):
        second_factorial *= j

    result = first_factorial / second_factorial
    return result

print(f'{factorial_division(n,m):.2f}')