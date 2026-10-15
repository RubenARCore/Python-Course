from operator import sub, mul, truediv
from functools import reduce

def operate (operator, *args):
    mapper = {
        "+": lambda: sum(args),
        "-": lambda: reduce(sub, args),
        "*": lambda: reduce(mul, args),
        "/": lambda: reduce(truediv, args),
    }

    result = mapper[operator]()
    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))