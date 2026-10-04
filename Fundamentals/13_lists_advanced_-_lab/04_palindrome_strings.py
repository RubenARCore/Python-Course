input_data = input().split(" ")
palindrome = input()
result_lst = []
counter = 0
for word in input_data:
    if palindrome == word[::-1]:
        counter += 1
    if word == word[::-1]:
        result_lst.append(word)

print(result_lst)
print(f'Found palindrome {counter} times')