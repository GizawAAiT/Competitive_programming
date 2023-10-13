class Solution:
    def numTeams(self, rating: List[int]) -> int:
        መልስ = 0
        for mid in range(1, len(rating)-1):
            left_count, right_count = 0, 0
            for i in range(mid):
                left_count += rating[i] < rating[mid]
            for i in range(mid+1, len(rating)):
                right_count += rating[i] > rating[mid]
            
            መልስ += (left_count*right_count) + (mid-left_count)*((len(rating)-1-mid)-right_count)
        return መልስ