arr = [1,1,1,2,2,2,3,3,4,4,4,5,5,7,7,7]
def removeDuplicates(arr):
    for i in range (len(arr)):
        if i < len(arr):
            while arr.count(arr[i]) > 2:
                arr.remove(arr[i])              
    print(arr)
    return len(arr)
    arr2 = []
    for i in range(len(arr)):
        if arr2.count(arr[i]) < 2:
            arr2.append(arr[i])
    print(arr2)
    return len(arr2)
print(removeDuplicates(arr))


