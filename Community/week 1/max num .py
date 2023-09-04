class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                a=int(str(nums[i])+str(nums[j]))
                b=int(str(nums[j])+str(nums[i]))
                if b>a:
                    nums[i],nums[j]=nums[j],nums[i]
        answer="".join(str(n) for n in nums)
        answer=int(answer)
        answer=str(answer)
        return answer