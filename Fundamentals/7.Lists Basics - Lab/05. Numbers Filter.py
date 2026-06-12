n = int(input())

input_number_lst = []
final_lst = []

for i in range(n):
    input_number_lst.append(int(input()))

command = input()

if command == 'even':
    for number in input_number_lst:
        if number % 2 == 0 or number == 0:
            final_lst.append(number)
elif command == 'odd':
    for number in input_number_lst:
        if number % 2 != 0:
            final_lst.append(number)
elif command == 'negative':
    for number in input_number_lst:
        if number < 0:
            final_lst.append(number)
elif command == 'positive':
    for number in input_number_lst:
        if number >= 0:
            final_lst.append(number)

print(final_lst)