def fib(n):
    def fibIter(a, b, count):
        if count == 0:
            return b
        else:
            print(a)
            return fibIter(a + b, a, count - 1)

    return fibIter(0, 1, n)


x = int(input())
fib(x)
