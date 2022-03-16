from math import sqrt


def eratosthen(n):  # 2
    a = list(range(n+1))
    a[1] = 0
    ind = 2
    while ind <= sqrt(n):
        if a[ind] != 0:
            j = ind*2
            while j <= n:
                a[j] = 0
                j += ind
        ind += 1
    a = [i for i in a if i != 0]
    return a


print(eratosthen(100))
