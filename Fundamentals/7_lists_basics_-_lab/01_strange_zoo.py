lst = []

lst.append(input())
lst.append(input())
lst.append(input())

lst[0], lst[2] = lst[2], lst[0]

print(lst)