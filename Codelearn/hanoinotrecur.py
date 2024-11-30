def hanoi_iterative(n, source, auxiliary, target):
    # Tạo một từ điển để lưu trữ các cột
    pegs = {source: list(range(n, 0, -1)), auxiliary: [], target: []}
    
    # Tổng số bước di chuyển
    total_moves = 2**n - 1
    
    # Xác định hướng di chuyển dựa trên số đĩa
    moves = [source, auxiliary, target] if n % 2 == 0 else [source, target, auxiliary]

    for i in range(1, total_moves + 1):
        # Xác định cột nguồn và đích cho mỗi bước di chuyển
        from_peg = moves[i % 3]
        to_peg = moves[(i + 1) % 3]
        
        # Kiểm tra xem có thể di chuyển đĩa không
        if pegs[from_peg] and (not pegs[to_peg] or pegs[from_peg][-1] < pegs[to_peg][-1]):
            disk = pegs[from_peg].pop()
            pegs[to_peg].append(disk)
            print(f"Bước {i}: Di chuyển đĩa {disk} từ {from_peg} sang {to_peg}")
        else:
            # Nếu không thể di chuyển, đổi chiều
            from_peg, to_peg = to_peg, from_peg
            if pegs[from_peg]:
                disk = pegs[from_peg].pop()
                pegs[to_peg].append(disk)
                print(f"Bước {i}: Di chuyển đĩa {disk} từ {from_peg} sang {to_peg}")

# Sử dụng hàm
n = 3  # Số đĩa
hanoi_iterative(n, 'A', 'B', 'C')