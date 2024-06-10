# from functools import lru_cache


# @lru_cache
# def fib(n : int) -> int:
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# for i in range(0, 40):
#     print(f"{i} : {fib(i)}")

def f1():
    print("called F1")

def f2(f):
    f()

f2(f1)