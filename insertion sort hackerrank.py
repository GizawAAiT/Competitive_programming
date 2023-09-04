#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    
    t = arr[n-1]
    cur = n-2
    while cur>-1 and arr[cur]>t:
        arr[cur+1] = arr[cur]
        for _ in arr: print(_, end = ' ')
        print()
        cur += -1
    arr[cur+1] = t
    for _ in arr: print(_, end = ' ')
    
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
