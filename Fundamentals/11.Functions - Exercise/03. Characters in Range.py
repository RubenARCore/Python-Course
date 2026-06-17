a = ord(input())
b = ord(input())


def characters_range(a_, b_):
    result_ = []
    for x in range(a_ + 1, b_ ):
        result_.append(chr(x))

    return result_

print(" ".join(characters_range(a, b)))