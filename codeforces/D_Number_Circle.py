n = int(input())

nums = [int(_ ) for _ in input().split()]
nums.sort()
even = [nums[i] for i in range(0, n, 2)]
odd = [nums[i] for i in range(1, n, 2)]
odd.reverse()
odd.extend(even)
def check(odd):
    for i in range(n):
        # print((i,n))
        if odd[i] >= (odd[i-1] + odd[(i+1)%n]):
            # print('jesba')
            return False
    return True
if check(odd):
    print('YES')
    for _ in odd:
        print(_, end=' ')
else:
    print('NO')