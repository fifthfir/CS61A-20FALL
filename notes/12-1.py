def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

def fact_times(n, k):
    if n == 0:
        return k
    else:
        return fact_times(n - 1, n * k)
    