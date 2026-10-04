budget = float(input())
gpu = float(input())
cpu = float(input())
ram = float(input())

gpu_price = gpu * 250
cpu_price = gpu_price * 0.35 * cpu
ram_price = gpu_price * 0.10 * ram

total_price = cpu_price + ram_price + gpu_price

if gpu > cpu:
    total_price -= total_price * 0.15

if total_price > budget:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')
else:
    print(f'You have {budget - total_price:.2f} leva left!')


