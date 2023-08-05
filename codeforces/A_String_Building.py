t = int(input())
def solve(s):
    if len(s) == 1:
        return 'NO'
    s += "C"
    s = "C" + s
    for i in range(1, len(s)-1):
        if s[i] not in [s[i-1], s[i+1]]:
            return 'NO'

    return 'YES'

for _ in range(t):
    s = input()
    print(solve(s))
