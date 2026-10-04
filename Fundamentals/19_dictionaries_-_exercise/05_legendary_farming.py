import operator

junk_dict = {}
legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
flag = True

while flag:

    data = input().lower().split()


    for i in range(0,len(data), 2):
        if data[i + 1] == "shards":
            legendary_items["shards"] += int(data[i])
        elif data[i + 1] == "fragments":
            legendary_items["fragments"] += int(data[i])
        elif data[i + 1] == "motes":
            legendary_items["motes"] += int(data[i])
        else:
            if data[i + 1] not in junk_dict:
                junk_dict[data[i + 1]] = int(data[i])
            else:
                junk_dict[data[i + 1]] += int(data[i])
        if legendary_items["shards"] >= 250 or legendary_items["fragments"] >= 250 or legendary_items["motes"] >= 250:
            flag = False
            break

max_item = max(legendary_items.items(), key=operator.itemgetter(1))[0]

if max_item == "shards":
    print(f"Shadowmourne obtained!")
    legendary_items["shards"] -= 250
elif max_item == "fragments":
    print(f"Valanyr obtained!")
    legendary_items["fragments"] -= 250
elif max_item == "motes":
    print(f"Dragonwrath obtained!")
    legendary_items["motes"] -= 250

for key, value in legendary_items.items():
    print(f"{key}: {value}")

for key, value in junk_dict.items():
    print(f"{key}: {value}")

