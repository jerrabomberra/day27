def add(n, *args, **kwargs):
    final = 0
    for i in args:
        final += i
    for key, value in kwargs.items():
        final += value
    final += n
    return final


print(add(1, 2, 3, a=4, b=5))



z = (lambda x, y : x + y)

print(z(1, 2))