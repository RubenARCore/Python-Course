bullet_price = int(input())
barrel_size = int(input())

bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))

intelligence_value = int(input())

bullets_in_barrel = barrel_size
bullets_fired = 0

while bullets and locks:

    bullet = bullets.pop()
    lock = locks[0]

    bullets_in_barrel -= 1
    bullets_fired += 1

    if bullet <= lock:
        print("Bang!")
        locks.pop(0)
    else:
        print("Ping!")

    if bullets_in_barrel == 0 and bullets:
        print("Reloading!")
        bullets_in_barrel = barrel_size

if not locks:
    money_earned = intelligence_value - bullets_fired * bullet_price
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")