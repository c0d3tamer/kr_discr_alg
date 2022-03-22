'''
1 НОД
'''


def evclid_nod(a, b):  # 1
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b


print(evclid_nod(int(input()), int(input())))
