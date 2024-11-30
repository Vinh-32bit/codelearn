import math
S = 5
def diagonal_of_cross(S):
    r=math.sqrt(S*1.8+(1/9*S*1.8))
    return round(r,1)
print(diagonal_of_cross(S))
