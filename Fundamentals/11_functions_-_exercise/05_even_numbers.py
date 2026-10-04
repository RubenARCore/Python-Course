n = list(map(int, input().split()))

def even_number(n_):
    result = []
    for num in n_:
        if num % 2 == 0:
            result.append(num)

    return result

print(f'[{", ".join(map(str, even_number(n)))}]')
