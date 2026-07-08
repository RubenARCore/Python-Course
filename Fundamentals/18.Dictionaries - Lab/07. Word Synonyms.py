n = int(input())
synonyms = {}

for i in range(n):

    word = input()

    if word not in synonyms:
        synonyms[word] = {}

    synonym = input()
    synonyms[word][i] = synonym

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value.values())}")