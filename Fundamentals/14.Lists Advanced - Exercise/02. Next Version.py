n = list(map(int, input().split(".")))

if n[-1] != 9:
    print(f'{n[0]}.{n[1]}.{n[2]+1}')