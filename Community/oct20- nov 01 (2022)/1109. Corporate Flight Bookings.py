class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)
        
        for b in bookings:
            res[b[0]-1] += b[2]
            res[b[1]] -= b[2]
        for i in range(1,n):
            res[i] += res[i-1]
        return res[:n]