n = int(input())

positive_lst = []
negative_lst = []

for i in range(n):
    data = int(input())
    if data > 0:
        positive_lst.append(data)
    else:
        negative_lst.append(data)

print(positive_lst)
print(negative_lst)
print(f'Count of positives: {len(positive_lst)}')
print(f'Sum of negatives: {sum(negative_lst)}')


