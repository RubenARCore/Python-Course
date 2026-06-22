n = list(map(int, input().split(" ")))
factor = int(input())


lst = [i * factor for i in n]

average = sum(lst) / len(lst)

lst_result = [ x for x in lst if x >= average ]

if len(lst_result) >= len(n) / 2:
    print(f'Score: {len(lst_result)}/{len(n)}. Employees are happy!')
else:
    print(f'Score: {len(lst_result)}/{len(n)}. Employees are not happy!')



# The most stupid solution... but it works.
# Sorry to whoever will read and, God forbid, use this code...
# I have a small child, I haven't slept for days, and honestly that's about my skill level...
