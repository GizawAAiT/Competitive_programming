class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        no=set(str(x) for x in range (10))
        operations=["*","-","/","+"]
        a="3333"
        op=[]
        nums=[]
        i=0
        while i < len(s):
            if s[i] in no:
                j=i
                while i<len(s) and s[i] in no: 
                      i+=1                        
                nums.append(int(s[j:i]))
            elif s[i] in operations:
                op.append(str(s[i]))
                i+=1
            else:
                i+=1
        print ("nums=",nums,"ope=" ,op)
        st=[]
        st.append(nums[0])
        for i in range( len(op)):
            if op[i]=="-":
                st.append(-(int(nums[i+1])))
            elif op[i]=="/":
                if st[-1]<0:
                    st[-1]=-(-(st[-1])//int(nums[i+1]))
                else:
                    st[-1]=st[-1]//int(nums[i+1])
            elif op[i]=="*":
                st[-1]=st[-1]*int(nums[i+1])
            else:
                st.append((int(nums[i+1])))
        return sum( st)