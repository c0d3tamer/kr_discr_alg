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


print(euler(int(input())))
