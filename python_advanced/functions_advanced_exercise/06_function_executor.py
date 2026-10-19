def func_executor(*args):
    result = []
    for func, func_args in args:
        res = func(*func_args)
        result.append(f"{func.__name__} - {res}")

    return "\n".join(result)