result = [0]
def mergeSort(arr, l, r, result):
    if  l >= r:
        return True

    m = l + (r-l)//2
    left = mergeSort(arr, l, m, result) 
    right = mergeSort(arr, m+1, r, result)
    return merge(arr, l, r, m, result) and left and right

def merge(arr, l, r, m, result):    
    L, R = arr[l:m+1], arr[m+1:r+1]
    """3 conditions:
    1. L[-1] < R[0] True
    2. R[-1] < L[0] True
    3. Otherwise....False
    """   
    if not(L[-1] < R[0] or R[-1] < L[0]):
        return False 
    
    if R[-1] < L[0]: 
        k = l
        for i in range(len(R)):
            arr[k] = R[i]
            k += 1
        for i in range(len(L)):
            arr[k] = L[i]
            k += 1
        result[0] += 1

    return True
        

t = int(input())
for _ in range(t):
    m = int(input())
    perm = [int(_) for _ in input().split()] #
    result[0] = 0 
    if mergeSort(perm, 0, m-1, result) :
        print(result[0])
    else:
        print(-1)

