# mymath/__init__.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def power(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

def cos(x, terms=10):
    result = 0
    for n in range(terms):
        sign = (-1) ** n
        result += sign * power(x, 2 * n) / factorial(2 * n)
    return result
