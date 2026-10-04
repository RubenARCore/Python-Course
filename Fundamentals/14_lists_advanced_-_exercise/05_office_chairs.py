n = int(input())
flag = True
free_chairs_counter = 0
for i in range(1, n+1):
    data = input().split()
    chairs_count = len(list(map(str, data[0])))
    visitors = int(data[1])
    if chairs_count < int(data[1]):
        print(f'{int(data[1]) - chairs_count} more chairs needed in room {i} ')
        flag = False
    else:
        free_chairs_counter += chairs_count - visitors

if flag:
    print(f'Game On, {free_chairs_counter} free chairs left')