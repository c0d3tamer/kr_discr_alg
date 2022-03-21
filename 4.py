"""
Функция Мебиуса
"""

from math import sqrt

n = int(input("Введите число: "))


Ans = []
count_divs = 0
d = 2
while d * d <= n:
    if n % d == 0:
        Ans.append(d)
        n //= d
        count_divs += 1
    else:
        d += 1
if n > 1:
    Ans.append(n)
    count_divs += 1


for i in range(0, count_divs):
    for j in range(i+1, count_divs):
        if Ans[i] == Ans[j]:
            print("Функция Мйбиуса = 0")
            exit()
print("Функция Мйбиуса = 1" if count_divs % 2 == 0 else "Функция Мйбиуса = -1")
