def fibSum(n):
    if n == 1:
        return 1
    module = 10**9+7
    a = 1
    b = 1
    f = [a,b]
    sum = (a+b) % module
    while len(f) < n:
        # b = (a + b) % module gây sai số khi số quá lớn
        # a = (b - a) % module
        a, b = b, (a + b) % module
        f.append(b)
        sum = (sum + b) % module
    return sum
print(fibSum(120))