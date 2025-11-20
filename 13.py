def f(row, n, queens, solutions):
    # все ферзи расставлены
    if row == n:
        solutions.append(queens[:])
        return
    
    # Пробуем поставить ферзя в каждый столбец
    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            f(row + 1, n, queens, solutions)
            queens[row] = -1  # Backtrack

def is_safe(queens, row, col):
    # Проверяем безопасность позиции
    for i in range(row):
        if queens[i] == col or abs(queens[i] - col) == abs(i - row):
            return False
    return True

# Использование
n = 8
queens = [-1] * n
solutions = []
f(0, n, queens, solutions)
print(f"Найдено решений: {len(solutions)}")