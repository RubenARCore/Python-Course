n = input().split(", ")
result_list = []


def palindrome(num):
    for i in range(0, len(num)):

        reversed_n = list(reversed(num[i]))

        if list(num[i]) == list(reversed_n):
            result_list.append(True)
        else:
            result_list.append(False)

    return result_list

palindrome(n)

for i in range(0, len(n)):
    if result_list[i]:
        print('True')
    else:
        print('False')


