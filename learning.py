def add(n, *args, **kwargs):
    sum = 0
    for i in args:
        sum += i
    for key, value in kwargs.items():
        sum += value
    sum += n
    return sum


print(add(1, 2, 3, 4, a=5, b=6))

list = [1, 2, 3]
y = []

y = [a * 3 for a in list]
print(y)
