n = int(input())
key_word = input()

first_lst = []
second_lst = []

for i in range(n):
    first_lst.append(input())

for i in range(n):
    if key_word in first_lst[i]:
        second_lst.append(first_lst[i])

print(first_lst)
print(second_lst)