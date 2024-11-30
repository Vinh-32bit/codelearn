def hanoi(n, source, aux, target):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ cột {source} sang cột {target}")
        return
    
    hanoi(n-1, source, target, aux)
    print(f"Di chuyển đĩa {n} từ cột {source} sang cột {target}")
    hanoi(n-1, aux, source, target)

n = 2  
hanoi(n, 'A', 'B', 'C')