n = list(map(int, input().split(" ")))
factor = int(input())


lst = [i * factor for i in n]

average = sum(lst) / len(lst)

lst_result = [ x for x in lst if x >= average ]

if len(lst_result) >= len(n) / 2:
    print(f'Score: {len(lst_result)}/{len(n)}. Employees are happy!')
else:
    print(f'Score: {len(lst_result)}/{len(n)}. Employees are not happy!')



# Най идиотското решение... Но работи.
# Извинявам се на този, който ще чете и недай боже ползва този код...
# Имам малко дете, не съм спал от дни, а и като цяло толкова си мога...
