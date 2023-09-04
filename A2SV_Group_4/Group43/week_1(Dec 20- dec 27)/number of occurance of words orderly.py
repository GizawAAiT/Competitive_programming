# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
words = []
for i in range(n):
    words.append(input())
dic, order = {}, []
for w in words:
    if w in dic: dic[w]+=1
    else:
        order.append(w) 
        dic[w]=1
print(len(order)) 
for w in order:
    print(dic[w], end=' ') 
    

