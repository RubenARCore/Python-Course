data = input()
result = ""
current_string = ""
current_number = ""

for ch in data:

    if ch.isdigit():
        current_number += ch


    else:
        if current_number:
            result += current_string.upper() * int(current_number)
            current_string = ""
            current_number = ""


        current_string += ch


result += current_string.upper() * int(current_number)

print(f"Unique symbols used: {len(set(result))}")
print(result)