count_pages = int(input())
pages_per_hour = int(input())
days = int(input())

result = count_pages / pages_per_hour / days
# print(f'{result:.0f}')
print(int(result))