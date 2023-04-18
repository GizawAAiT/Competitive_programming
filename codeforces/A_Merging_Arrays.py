n, m = (int(_) for _ in input().split())

nums1 = [int(_) for _ in input().split()]
nums2 = [int(_) for _ in input().split()]
i,j = 0,0 
merged = []

while i<n and j<m:
    if nums1[i]<nums2[j]:
        merged.append(nums1[i])
        i+=1
    else:
        merged.append(nums2[j])
        j+=1

while i<n:
    merged.append(nums1[i])
    i+=1

while j<m:
    merged.append(nums2[j])
    j+=1

print(*merged)