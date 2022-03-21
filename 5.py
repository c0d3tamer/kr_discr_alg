"""
Функция Эйлера
"""

from math import sqrt


def euler(n: int) -> int:
    result = n
    for i in range(2, n):
        if (n % i == 0):
            while (n % i == 0):
                n //= i
            result -= result // i
    if (n > 1):
        result -= result // n
    return result


def evclid_nod(a: int, b: int) -> int:  # 1
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b


def euler_2(n: int) -> int:
    cnt = 0
    for i in range(1, n):
        if evclid_nod(n, i) == 1:
            cnt += 1
    return cnt


n = int(input())

print(euler(n))
print(euler_2(n))
