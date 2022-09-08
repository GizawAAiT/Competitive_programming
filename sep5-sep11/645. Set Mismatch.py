class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        repeated = None
        missed = None
        
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==2:
                missed = nums[i-1]+1  
                print(missed)
            if nums[i]-nums[i-1]==0:
                repeated = nums[i]
        choice = [1,len(nums)] 
        
        if missed == None:
            missed = choice[int(nums[-1]!=len(nums))]
            
        return [repeated,missed]
                
     