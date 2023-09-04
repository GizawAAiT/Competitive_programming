class Solution:
    def carFleet(self, target, position, speed):
        
        time_stack = [0]
        
        for d, v in (sorted([(target-position[i],speed[i]) for i in range(len(speed))])):
            print((d,v))
            t = d/v 
            if t>time_stack[-1]:
                time_stack.append(t)
                print(time_stack)
        return len(time_stack)-1
            