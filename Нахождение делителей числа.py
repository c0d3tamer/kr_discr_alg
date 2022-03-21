from math import sqrt, floor


n = int(input("Введите число: "))
a = []


for i in range(2, int(floor(sqrt(n)))):
    if n % i == 0:
        a.append(i)
    if n % (n/i) == 0 and (n/i) % 1 == 0:
        a.append(int(n/i))
print(f"Делители: {sorted(a)}")
