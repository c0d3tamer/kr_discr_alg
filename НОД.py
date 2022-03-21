num1, num2 = map(int, (input().split()))


def gcd_common_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


if __name__ == '__main__':
    print(f"num1: {num1}", "--- ", f"num2: {num2}")
    my = gcd_common_division(num1=num1, num2=num2)
    print(f"GCD: {my}")
