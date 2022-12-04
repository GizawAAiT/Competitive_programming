class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        sufix=[1]
        A=[]
        num=list(reversed(nums))
        for i in range(len(nums)):
            prefix.append(prefix[-1]*nums[i])
            sufix.append(sufix[-1]*num[i])
        prefix.append(1)
        sufix=list(reversed(sufix))
        sufix.insert(0,1)
        
        for i in range(len(nums)):
            A.append(prefix[i]*sufix[i+2])
        print(prefix,"\n",sufix)
        return A