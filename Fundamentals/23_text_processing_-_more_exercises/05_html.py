h1 = input()
article = input()
lst = []
while True:
    data = input()
    if data == "end of comments":
        break
    lst.append(data)

print(f"<h1>\n  {h1}\n</h1>")
print(f"<article>\n  {article}\n</article>")
for word in lst:
    print(f"<div>\n  {word}\n</div>")