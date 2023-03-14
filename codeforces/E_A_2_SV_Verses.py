n, a , b = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]

left = result = 0 
def inBound(x):
    return x<=b and x>=a
for right in range(n):
    if not inBound(nums[right]) and inBound(nums[left]):
        x = right-left
        result += ((x+1)/2)*x 
        left = right
    elif inBound(nums[right]) and left==-1 or not inBound(nums[left]):
        left=right
if inBound(nums[left]):
    x = n-left 
    # print(x)
    result += ((x+1)/2)*x
print(int(result))