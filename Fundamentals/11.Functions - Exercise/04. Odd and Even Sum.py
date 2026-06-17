n = int(input())

def odd_even_sum(number):
    odd_sum = 0
    even_sum = 0

    while number > 0:
        single_digit = number % 10

        if single_digit % 2 == 0:
            even_sum += single_digit
            number //= 10
        else:
            odd_sum += single_digit
            number //= 10

    return odd_sum, even_sum

odd, even = odd_even_sum(n)
print(f'Odd sum = {odd}, Even sum = {even}')

