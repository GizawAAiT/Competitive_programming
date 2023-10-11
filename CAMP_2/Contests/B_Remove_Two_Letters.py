t = int(input())
for _ in range(t):
    mod = 5* (10**9)
    n = int(input())
    s = input()
    hash_val = 0
    for i in range(n):
        hash_val += (ord(s[i])-96) * pow(27, i, mod)
    
    diff_substrings = set()
    # subtract the first two characters:
    hash_val -= (ord(s[0])-96) + (ord(s[1])-96)*27
    hash_val //= 27*27

    diff_substrings.add(hash_val)
    for i in range(2, n):
        hash_val += (ord(s[i-2]) - ord(s[i]) )* (pow(27, i-2, mod))
        diff_substrings.add(hash_val)
    print(len(diff_substrings))