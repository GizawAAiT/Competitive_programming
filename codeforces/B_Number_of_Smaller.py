n,m = (int(_) for _ in input().split())
nums1=[int(_) for _ in input().split()]
nums2=[int(_) for _ in input().split()]
nums1.sort()
l=0

for i in range(len(nums2)):
    while l<len(nums1) and nums1[l]< nums2[i]:
        l+=1
    print(l, end=' ')
    
