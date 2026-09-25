box_of_clothes = list(map(int, input().split()))
capacity = int(input())
result = 0

while box_of_clothes:
    sum_of_clothes = 0

    while True:

        sum_of_clothes += box_of_clothes.pop()

        if sum_of_clothes == capacity:
            result += 1
            break
        elif len(box_of_clothes) == 0:
            result += 1
            break
        elif sum_of_clothes + box_of_clothes[-1] > capacity:
            result += 1
            break

print(result)