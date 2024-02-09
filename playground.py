# kwargs can be used

def mul(n, *args, **kwargs):
    prod = 1
    for key, value in kwargs.items():
        prod *= value
    for q in args:
        prod *= q
    return prod * n


print(mul(2, 2, 1, a=2, b=3))
