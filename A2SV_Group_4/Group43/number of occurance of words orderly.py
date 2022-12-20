# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
for i in range(n):
    words.append(input())

dic, s, order = {}, set(), []
for w in words:
    if w in dic:
        dic[w]+=1
    else: dic[w]=1
    if w not in s:
        s.add(w)
        order.append(w)
print(len(order))
for w in order:
    print(dic[w], end=' ')

