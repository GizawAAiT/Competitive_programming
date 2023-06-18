s = input()
i, j = 0, len(s)-1
def rec(s):
    total_caps = 0
    for c in s:
        total_caps += int(c.isupper())
    
    answer = min(total_caps, len(s)-total_caps)
    # print(total_caps)
    caps = 0
    for i in range(len(s)):
        caps += int(s[i].isupper())
        answer = min(answer,(i+1-caps) + (total_caps - caps))

    return answer 
print(rec(s))


"""
AaaAaAAaaA|aaaAaaaA
i-caps,   | upper_cases - caps

"""