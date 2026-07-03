class Party:
    def __init__(self):
        self.people = []


party = Party()

data = input()
while data != "End":
    party.people.append(data)
    data = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')