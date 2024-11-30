import math
def cut_cake(a,b,c):
    r = math.gcd(a,b,c)
    return r
print(cut_cake(2,4,2))