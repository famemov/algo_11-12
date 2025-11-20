def f(n, current=""):
    # достигли нужной длины
    if len(current) == n:
        return [current]
    # добавляем 0 и 1
    result = []
    result.extend(f(n, current + "0"))
    result.extend(f(n, current + "1"))
    return result

print(f(2))  # ['00', '01', '10', '11']