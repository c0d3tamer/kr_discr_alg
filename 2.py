"""
2 Решето этаросфена
"""

from math import sqrt


def eratosthen(n):  # 2
    a = list(range(n+1))
    a[1] = 0
    for ind in range(2, int(sqrt(n))+1):
        if a[ind] != 0:
            j = ind*2
            while j <= n:
                a[j] = 0
                j += ind
    a = set(a)
    a.remove(0)
    return a


print(*eratosthen(100))
