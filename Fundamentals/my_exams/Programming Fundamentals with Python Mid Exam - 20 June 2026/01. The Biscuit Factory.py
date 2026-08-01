biscuits_per_worker = int(input())
number_of_workers = int(input())
competing_factory = int(input())
biscuits_count = 0
laziness_loses = 0
difference = 0
for i in range(1,31):
    if i % 3 == 0:
        laziness_loses += int(biscuits_per_worker * number_of_workers * 0.75)
    else:
        biscuits_count += biscuits_per_worker * number_of_workers

biscuits_count += laziness_loses

if biscuits_count > competing_factory:
    difference = (biscuits_count - competing_factory) / competing_factory * 100
    print(f'You have produced {int(biscuits_count)} biscuits for the past month.')
    print(f'You produce {difference:.2f} percent more biscuits.')
else:
    difference = (competing_factory - biscuits_count) / competing_factory * 100
    print(f'You have produced {int(biscuits_count)} biscuits for the past month.')
    print(f'You produce {difference:.2f} percent less biscuits.')