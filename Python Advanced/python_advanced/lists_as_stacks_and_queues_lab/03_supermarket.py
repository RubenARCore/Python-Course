from collections import deque

deque = deque()

while True:
    data = input()
    if data == "Paid":
        for item in deque:
            print(item)
        deque.clear()
        continue

    if data == "End":
        print(f"{len(deque)} people remaining.")
        break

    deque.append(data)

