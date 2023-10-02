class TrieNode:
    def __init__(self):
        self.children = [(None, 0)]* 26



N = int(input())
strings = []
root = TrieNode()
for _ in range(N):
    s = input() # abc
    strings.append(s)
    cur = root
    for char in s:
        indx = ord(char)-ord("a")
        if not cur.children[indx][0]:
            cur.children[indx] = [TrieNode(), 1]
        else:
            cur.children[indx][1] += 1
        cur = cur.children[indx][0]

# result = []
for s in strings:
    cur = root
    ans = 0
    for char in s:
        indx = ord(char)-ord("a")
        if cur.children[indx][1] > 1:
            ans += 1
        else:
            break
        cur = cur.children[indx][0]
    print(ans)


