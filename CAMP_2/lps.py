pattern = "abacabacd"
lps = [0 for _ in range(len(pattern))]
left = 0
for right in range(1, len(pattern)):
    if pattern[left] == pattern[right]:

        lps[right] = left +1
        left += 1

    else:
        left = 0

    # elif left >0:
    #     lps[right] = lps[left-1]
    #     left = lps[left-1]


print(lps)
     