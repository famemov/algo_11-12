def f(n):
    #если одна цифра
    if n < 10:
        return n
    #если несколько
    return n%10 + f(n//10)
print(f(12345))