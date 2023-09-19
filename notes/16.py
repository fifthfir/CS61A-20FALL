def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x += 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
total = b(3) + b(4)

