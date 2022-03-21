"""
3 Делители числа
"""

from math import sqrt


def del_cnt(n):
    cnt = 0
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            cnt += 1
    return cnt*2


print(del_cnt(int(input())))
