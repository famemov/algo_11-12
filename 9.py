def sor(n, i=0):
    # дошли до конца массива
    if i >= len(n)-1:
        return True
    # элемент больше следующего - массив не отсортирован
    if n[i]>n[i+1]:
        return False
    # проверяем остальную часть массива
    return sor(n,i+1)
print(sor([1,2,3,2,5]))
print(sor([1,2,3,4,5]))