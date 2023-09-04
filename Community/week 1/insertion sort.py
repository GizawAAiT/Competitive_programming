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
    # Write your code here
    tempo=arr[-1]
    for i in range (len(arr)-2,-1,-1):
        if tempo<arr[i]:
            arr[i+1]=arr[i]
            for i in range(len(arr)):
                print(str(arr[i]),end=" ")
           
        else:
            arr[i+1]=tempo
            for i in range(len(arr)):
                print(str(arr[i]),end=" ")
            break
        print()
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
