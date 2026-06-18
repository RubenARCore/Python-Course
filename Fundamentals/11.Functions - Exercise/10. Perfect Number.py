n = int(input())


def perfect_number(n):
    result_list = []
    for i in range(1, n - 1):
        if n % i == 0:
            result_list.append(i)

    return sum(result_list) == n

if perfect_number(n):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')