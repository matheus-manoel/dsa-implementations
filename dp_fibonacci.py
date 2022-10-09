memo = [None] * 100


def fib(n):
    if memo[n]:
        return memo[n]

    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib(n-2) + fib(n-1)

    memo[n] = res
    return res


print(fib(80))
