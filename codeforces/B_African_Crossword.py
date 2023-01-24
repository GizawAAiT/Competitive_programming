from collections import Counter


n, m = [int(x) for x in input().split()]
words = []
for _ in range(n):
    words.append(input())

#keep the count of each words vertically and horizontally.
hor, ver = {}, {}
for i in range(n):
    hor[i] = Counter(words[i])
for j in range(m):
    ver[j] = Counter([words[i][j] for i in range(n)])
# print('hor:',hor,'\nver:',ver)    
for i in range(n):
    for j in range(m):
        if hor[i][words[i][j]] == 1 and ver[j][words[i][j]] == 1:
            print(words[i][j], end='')

