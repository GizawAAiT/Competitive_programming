s = input()
# count = [0]
memo = {}
def backtrack(i, size):
    if i >= size:
        # count[0] += 1
    
        return 1
    if (i, size) not in memo:

        n = backtrack(i + 1, size)
        m = backtrack(i + 2, size)
        memo[(i, size)] = m + n
    return memo[(i, size)]

answer = 1
for char in s:
    if char in ['w', 'm']:
        answer = 0
        break

if answer == 0 :
    print(0)

else:
    ans = [1.0]
    i = 1
    while i < len(s):
        if s[i] == s[i-1] and s[i] in ['u', 'n'] :
            right = i
            while right < len(s) and s[right] == s[i]:
                right += 1
            
            ans[0] *= backtrack(1, right-i+1)
            # ans[0] %= 10**9 + 7
            i = right
        i += 1    

    print(int(ans[0] % (10**9 +7)))

