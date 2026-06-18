n = input().split(", ")
result_list = []
for i in range(0, len(n)):

    reversed_n = list(reversed(n[i]))

    if list(n[i]) == list(reversed_n):
        print("True")
    else:
        print("False")