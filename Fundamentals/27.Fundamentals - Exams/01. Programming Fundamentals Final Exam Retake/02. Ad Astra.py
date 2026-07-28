import re
days = 0
data = input()
result = []
pattern = r"#([A-Za-z\s]+)#(\d{2}/\d{2}/\d{2})#(\d+)#|\|([A-Za-z\s]+)\|(\d{2}/\d{2}/\d{2})\|(\d+)\|"

matches = re.findall(pattern, data)

for match in matches:
    _ = [x for x in match if x != ""]
    days += int(_[2])
    result.append(_)

print(f"You have food to last you for: {days // 2000} days!")

for match in result:
    print(f"Item: {match[0]}, Best before: {match[1]}, Nutrition: {match[2]}")