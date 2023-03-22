n = int(input())
nums = [int(_) for _ in input().split()]
parity = nums[0]%2
changed = False
for n in nums:
    if n%2 != parity:
        changed = True
        break
if changed:
    print(*sorted(nums))
else:
    print(*nums)
