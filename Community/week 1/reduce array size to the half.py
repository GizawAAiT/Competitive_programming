class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        fr=[]
        arr=sorted (arr)
        c=1
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                c+=1
            else:
                fr.append(c)
                c=1
        fr.append(c)
        fr=sorted(fr)
        p=0
        co=0
        for i in range (len(fr)):
            if p>=len(arr)/2:
                break
            p+=fr[-1-i]
            co +=1
            
        return co
        
