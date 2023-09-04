class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return (nums)
        if len(nums)==1:
            return [str(nums[0])]
        st = []
        
        i = 1
        t = 0
        while i < len(nums):
            if nums[i-1] != nums[i]-1 and i-t==1:
                
                st.append(str(nums[t]))
                t+=1
            elif nums[i-1] != nums[i]-1 and i-t!=1:
                c = (str(nums[t])+"->"+str(nums[i-1]))
                st.append(c)
                t=i
            
            i+=1
        if t == len(nums)-1:
            st.append(str(nums[t]))
        else:
            c = (str(nums[t])+"->"+str(nums[-1])) 
            st.append(c)
            
        return (st)