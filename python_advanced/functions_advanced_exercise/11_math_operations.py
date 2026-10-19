def math_operations(*args, **kwargs):
    keys = ["a", "s", "d", "m"]

    for i, num in enumerate(args):
        current_key = keys[i % 4]

        if current_key == "a":
            kwargs["a"] += num
        elif current_key == "s":
            kwargs["s"] -= num
        elif current_key == "d":
            if num != 0:
                kwargs["d"] /= num
        elif current_key == "m":
            kwargs["m"] *= num

    sorted_operations = sorted(
        kwargs.items(),
        key=lambda item: (-item[1], item[0])
    )

    result = []
    for key, value in sorted_operations:
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))