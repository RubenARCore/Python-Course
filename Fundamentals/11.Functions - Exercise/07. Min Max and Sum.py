n = list(map(int, input().split()))

def min_max_sum(n_):
    return min(n_), max(n_), sum(n_)

min_value, max_value, total_sum = min_max_sum(n)

print(f'The minimum number is {min_value}')
print(f'The maximum number is {max_value}')
print(f'The sum number is: {total_sum}')