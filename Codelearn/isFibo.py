def isFibonacci(k):
    a,b=1,1
    fib = [a,b]
    while b < k :
        a,b = b,a+b
        fib.append(b)
    return k in fib
    