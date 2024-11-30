#(u,v,t)
def gift(n,k):
    employees = [0,]*n
    for j in range (len(k)):
        u, v, t = k[j]  # Lấy u,v,t
        if v >= u:
            for i in range(u-1, v):
                employees[i] += t
    return employees
print(gift(3,[[2,3,1],[2,3,1]]))