n = int(input())
dic = {}
for _ in range(n):
    p, q = (int(_) for _ in input().split())
    dic[p] = q

def check(prices):
    q = dic[prices[0]]
    for p in prices:
        if dic[p] < q:
            return False
        q = dic[p]
    return True
if not check(sorted(dic.keys())):
    print('Happy Alex')
else:
    print('Poor Alex')

