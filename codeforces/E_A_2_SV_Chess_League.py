def mergeSort(l, r, arr):
    if l<r:
        mid = l + (r-l)//2
        L, R = arr[:mid+1],  arr[mid+1:]
        mergeSort(l, mid, L)
        mergeSort(mid, r, R)
        # Merge:
        merged = []
        i, j = 0, 0
        while i < len(L) or j < len(R):
            a, b = L[i] if i < len(L) else None, R[j] if j < len(R) else None
            merged.append(a if a and b and )



n, k = (int(_) for _ in input().split())
arr = [int(_) for _ in input().split()]

l, r = 0, len(arr)-1
