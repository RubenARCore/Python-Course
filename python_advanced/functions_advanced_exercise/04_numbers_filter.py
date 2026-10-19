def even_odd_filter(**kwargs):
    filtered_data = {}

    for key, values in kwargs.items():
        if key == "even":
            filtered_data[key] = [x for x in values if x % 2 == 0]
        elif key == "odd":
            filtered_data[key] = [x for x in values if x % 2 != 0]

    sorted_data = dict(sorted(filtered_data.items(), key=lambda item: len(item[1]), reverse=True))

    return sorted_data

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))