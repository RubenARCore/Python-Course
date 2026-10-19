def age_assignment(*args, **kwargs):
    result = {}

    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            result[name] = kwargs[first_letter]

    sorted_people = sorted(result.items(), key=lambda x: x[0])

    lines = []
    for name, age in sorted_people:
        lines.append(f"{name} is {age} years old.")

    return "\n".join(lines)

print(age_assignment("Peter", "George", G=26, P=19))