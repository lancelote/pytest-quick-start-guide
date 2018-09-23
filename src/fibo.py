def fibonacci(num):
    i = 1
    x0, x1 = 0, 1
    if num == 0:
        return x0
    elif num == 1:
        return x1
    while i != num:
        i += 1
        x0, x1 = x1, x0 + x1
    return x1
