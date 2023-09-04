"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

from typing import List


class Solution:
    def findSolution(self, f, z: int) -> List[List[int]]:
        res, i, j = [], 1, 1
        while i <= z:
            if f.f(i,j)==z:
                res.append([i,j])
                j+=1
            elif f.f(i,j)>z:
                i+=1
                j=1 
            else:
                j+=1
        return res
        
        