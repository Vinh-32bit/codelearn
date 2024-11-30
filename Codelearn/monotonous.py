def isMonotonous(sequence):
    if len(sequence) <= 1:
        return True
    elif len(sequence) == 2:
        return sequence[0] !=  sequence[1]
    for i in range(len(sequence) - 2):
        print(f'i : {sequence[i]}  i+1: {sequence[i+1]}')
        print(f'i+1 : {sequence[i+1]}  i+2: {sequence[i+2]}')
        if (sequence[i] > sequence[i + 1] and sequence[i+1] > 
            sequence[i+2]) or (sequence[i] < sequence[i+1] 
                               and sequence[i+1]<sequence[i+2]):
            pass
        else:
            return False
    return True
print(isMonotonous([1,2,4,3,3]))