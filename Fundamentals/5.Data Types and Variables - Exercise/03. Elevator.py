number_of_people = int(input())
capacity = int(input())

if number_of_people % capacity == 0:
    print(int(number_of_people / capacity))

else:
    print(int(number_of_people / capacity) + 1)
