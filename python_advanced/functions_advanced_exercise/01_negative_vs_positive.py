def numbers(*args):

    positive = []
    negative = []

    def separate_numbers():
        for number in args:
            if number > 0:
                positive.append(number)
            else:
                negative.append(number)
    separate_numbers()

    def sum_positive():
        return sum(positive)

    def sum_negative():
        return sum(negative)

    return sum_positive(), sum_negative(), positive > negative

positive, negative, larger_number = numbers(*map(int, input().split()))

print(f"{negative}\n{positive}")
print("The negatives are stronger than the positives" if abs(negative) > positive else "The positives are stronger than the negatives")
