import re
pattern = r'>>(\w+)<<(\d+(?:\.\d+)?)!(\d+)'
total_sum = 0
lst_names = []
while True:
    data = input()
    if data == "Purchase":
        break

    matches = re.findall(pattern, data)

    if matches:
        lst_names.append(matches[0][0])
        price = matches[0][1]
        quantity = matches[0][2]
        total_sum += float(price) * int(quantity)

print("Bought furniture:")
for item in lst_names:
    print(item)
print(f"Total money spend: {total_sum:.2f}")