from collections import deque

rows, cols = map(int, input().split())
word = deque(list(input()))
long_string = deque()
temporary = []
for i in range(rows*cols):
    long_string.append(word[0])
    word.append(word.popleft())

for i in range(rows):
    for j in range(cols):
        temporary.append(long_string.popleft())
    if i % 2 == 0:
        print(*temporary, sep="")
        temporary.clear()
    else:
        temporary.reverse()
        print(*temporary, sep="")
        temporary.clear()