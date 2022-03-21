"""
Функция Эйлера
"""

n = int(input("Введите число: "))


result = n
for i in range(2, n):
    if (n % i == 0):
        while (n % i == 0):
            n //= i
        result -= result / i
if (n > 1):
    result -= result / n
print(f"Функция Эйлера = {result}")
