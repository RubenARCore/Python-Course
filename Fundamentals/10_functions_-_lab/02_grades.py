n = float(input())

def grades (data):

    if 2.00 <= data <= 2.99:
        return 'Fail'
    elif 3.00 <= data <= 3.49:
        return 'Poor'
    elif 3.50 <= data <= 4.49:
        return 'Good'
    elif 4.50 <= data <= 5.49:
        return 'Very Good'
    else:
        return 'Excellent'

print(grades(n))

