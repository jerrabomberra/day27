
def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper

@f1
def f(a):
    print(a)


f("Hi!")