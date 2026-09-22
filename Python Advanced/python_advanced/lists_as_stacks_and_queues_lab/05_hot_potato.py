from collections import deque

queue = deque(input().split())
n = int(input())

while len(queue) > 1:
    for _ in range(n - 1):
        queue.append(queue.popleft())

    removed = queue.popleft()
    print(f"Removed {removed}")

print(f"Last is {queue[0]}")