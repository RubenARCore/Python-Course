banned_words = input().split(", ")

data = input()

for word in banned_words:

    data = data.replace(word, f"{'*' * len(word)}")
print(data)