n = list(map(int, input().split()))

def sort_numbers(n_):

    return sorted(n_)

print(f'[{", ".join(map(str, sort_numbers(n)))}]')