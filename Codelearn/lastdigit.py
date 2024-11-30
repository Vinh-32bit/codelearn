import math
def lastDigitDiffZero(n):
    if n == 0:
        return 1
    value = 1
    last_digit = 0
    for i in range (1, n+1):
        value *= i
    while value % 10 == 0:
        value //= 10
    last_digit = int(value % 10)
    return last_digit
print(lastDigitDiffZero(25))
print(math.factorial(25))