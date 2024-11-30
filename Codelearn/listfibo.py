n = int(input("Enter n: "))
def fibo(n):
    a = 0
    b = 1
    f = [a,b]
    while len(f) < n:
        b = a + b
        #a = b(mới) - a = b(cũ)     |     a,b = b, b-a
        a = b - a
        f.append(b)
    print(f)
fibo(n)