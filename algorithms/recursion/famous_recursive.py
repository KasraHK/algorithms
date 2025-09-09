def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

def divide(x, y):
    if x < y:
        return 0
    return 1 + divide(x - y, y)

def mod(x, y):
    if x < y:
        return x
    return mod(x - y, y)

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, mod(x, y))

def combination(n, r):
    if r == 0 or r == n:
        return 1
    return combination(n - 1, r - 1) + combination(n - 1, r)