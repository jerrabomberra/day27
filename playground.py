# def add(*args):
#     print(args[2])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum


# # print(add(1, 2, 3, 4, 5, 6))


# def makeSentence(**words):
#     sentence = ""
#     for word in words.values():
#         sentence += word
#     return sentence


# print("Sentence:", makeSentence(a="Kwargs ", b="are ", c="awesome!"))


# kwargs can be used


def multi(n, *args, **kwargs):
    prod = n
    for key, value in kwargs.items():
        prod *= value
    for q in args:
        prod *= q
    return prod


print(multi(2, 2, 3, a=4, b=5, c=6))
