#Bạn được cho 2 số nguyên A,B. Bạn hãy đếm số lượng số trong khoảng [A,B] 
#sao cho số đó có số lượng lẻ ước nguyên dương.
# Ví dụ:
# Với A = 4, B = 4 thì ta có đáp án là 1 số thỏa điều kiện.
# Giải thích: 4 có 3 ước là 1,2,4 nên thỏa điều kiện để bài.
def solve(a,b):
    result = 0
    for num in range(a,b+1):
        count = 0
        for i in range(1, num+1):
            if  num % i == 0:
                count += 1
        if  count % 2 != 0:
            result += 1
            print(num)
    return result
print(solve(1,10))

            
