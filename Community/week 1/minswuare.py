from math import *
def min(l):
    print(ceil((l[0])/l[2])*ceil((l[1])/l[2]))
list1=list(map(int, input().rstrip().split()))
min(list1)