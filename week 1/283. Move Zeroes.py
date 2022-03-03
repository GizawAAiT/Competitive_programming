class Solution(object):
    def moveZeroes(self, n):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter=0
        i=0
        while i<len(n):
            if n[i]==0:
                n.pop(i)
                counter+=1
            else:
                i+=1
        for i in range(counter):
            n.append(0)
            
        