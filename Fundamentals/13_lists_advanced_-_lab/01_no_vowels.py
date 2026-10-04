n = list(input())

m = [m for m in n if not m.lower() in ['a', 'e', 'i', 'o', 'u']]

print("".join(m))

