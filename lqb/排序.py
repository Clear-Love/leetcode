import math


def f(i: int):
    if i == 1:
        return 1
    return i+f(i-1)
print(f(14))