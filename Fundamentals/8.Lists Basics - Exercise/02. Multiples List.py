factor = int(input())
count = int(input())

result_list = []

for i in range(count):

    result_list.append((factor * i) + factor)

print(result_list)