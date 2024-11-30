import math
def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True   
A = []
b = input("Nhập mảng: ").split()
A.extend(map(int, b))
def check(A):
    result = []
    for i in range(len(A)):
        sum_right = sum(A[:i])
        sum_left = sum(A[i+1:])
        if isPrime(sum_left) and isPrime(sum_right):
            result.append(i)
    return result
print(check(A))


        