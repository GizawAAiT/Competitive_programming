class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        print(len(trips))
        mass = [0]*1001
        #add when passanger get in to the car and dubtract when drop.
        for t in trips:
            mass[t[1]] += t[0]
            mass[t[2]] -= t[0] 
        
        # make the cumulative sum
        for i in range(1,len(mass)):
            mass[i] += mass[i-1]
            if mass[i]>capacity: return False 
        return mass[0] <= capacity
        