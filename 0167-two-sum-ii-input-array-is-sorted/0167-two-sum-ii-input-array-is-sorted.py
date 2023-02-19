class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Using two-pointer technique.
        low, high = 0, len(numbers)-1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1
        return []
