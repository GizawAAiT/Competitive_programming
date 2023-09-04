#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    d = {}
    l = [path[0]]
    countvalley = 0

    for i in range(1, steps):
        c=0
        if len(l)==1 and l[0]=="D":
            c=1
        if len(l)==0 or path[i] == l[-1]:
            l.append(path[i])
        else:
            l.pop()
        if c==1 and len(l)==0:
            countvalley+=1
    return countvalley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
