class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums=sorted(nums)
        answer=[nums[0],nums[-1]]
        for i in range (1,(len(nums)//2)):
            answer.append(nums[i])
            if answer[-2]==(answer[-1]+answer[-2])/2:
                answer[-1],answer[-2]=answer[-2],answer[-1]
                
            answer.append(nums[-i-1])
        if len(nums)%2==1:
            answer.append(nums[len(nums)//2])
            if answer[-2]==(answer[-1]+answer[-2])/2:
                answer[-1],answer[-2]=answer[-2],answer[-1]
        return answer        

            