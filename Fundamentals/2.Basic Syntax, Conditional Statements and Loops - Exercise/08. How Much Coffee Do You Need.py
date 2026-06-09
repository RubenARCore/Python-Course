n = input()
total_coffees = 0

while n != "END":

    if n.lower() in ("coding", "dog", "cat", "movie"):

        if n.isupper():
            total_coffees += 2
        else:
            total_coffees += 1

    n = input()

if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)