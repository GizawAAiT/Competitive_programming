class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        target=float(target)
        times=[]
        print len(position)
        for i in range(len(position)):
            times.append((target-position[i])/speed[i] )
        PositionTimePair=[[pos,time] for pos,time in zip(position, times)]
        st=[0]      
        for p,t in sorted(PositionTimePair)[::-1]:
            if st[-1]<t:
                st.append(t)    
        return len(st)-1