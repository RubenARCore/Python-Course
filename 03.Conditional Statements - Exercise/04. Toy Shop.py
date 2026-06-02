holiday_price = float(input())
puzzle_count = int(input())
toys_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_toys = (puzzle_count + toys_count + bears_count
              + minions_count + trucks_count)
total_sum = (puzzle_count * 2.6
            + toys_count * 3
            + bears_count * 4.10
            + minions_count * 8.20
            + trucks_count * 2)
if total_toys >= 50:
    total_sum = total_sum - total_sum * 0.25

total_sum = total_sum - total_sum * 0.1

if total_toys >= holiday_price:
    print(f'Yes! {total_toys - holiday_price:.2f} lv left.')
else:
    print(f'Not enough money! {holiday_price - total_sum:.2f} lv needed.')