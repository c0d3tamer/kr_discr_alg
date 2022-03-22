"""
Функция Мебиуса
"""
from math import sqrt


def mebius_func(n: int) -> int:
    nums = []
    devider = 2

    while devider * devider <= n:
        if n % devider == 0:
            nums += [devider]
            n //= devider
        else:
            devider += 1
    if n > 1:
        nums += [n]
    deviders_count = len(nums)

    # сравниваем количество элементов списка и кортежа(в кортеже не существует повторяющихся элементов)
    # если кол-во разное, слевовательно присудствует квадрат числа
    if len(nums) != len(set(nums)):
        return 0
    if deviders_count % 2 == 0:
        return 1
    return -1


print(mebius_func(3945))
