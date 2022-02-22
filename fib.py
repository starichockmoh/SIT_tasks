def fib(n):
    if n == 1:
        return 0
    if n in (2, 3):
        return 1
    return fib(n - 1) + fib(n - 2)


x = int(input())
print(fib(x))
