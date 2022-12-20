class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num2 == "0" or num1=="0": return "0"
        def mul(num1,n2,i):
            res=[0]*i
            carry=0
            for i in range(len(num1)):
                n1=int(num1[-1-i])
                p=n1*n2+carry
                res.append(p%10)
                carry=p//10
            if carry !=0: res.append(carry)
            return res
        bank=[mul(num1,int(num2[-1-i]),i) for i in range(len(num2))]  
        def add(arr1,arr2):
            res,carry=[],0
            while arr1 or arr2 or carry:
                n1=arr1.pop(0) if arr1 else 0
                n2 = arr2.pop(0) if arr2 else 0
                s=carry+n1+n2
                res.append(s%10)
                carry=s//10
            return res
        ans=[]
        while len(bank)>0:
            ans=add(ans,bank.pop())
        ans=[str(i) for i in ans]
        return "".join(list(reversed(ans)))
        # for i in range(len(num2)):
        #     ans = mul(ans,int(num2[-1-i]),i)
        # ans=[str(i) for i in ans] 
        # return "".join(list(reversed(ans)))
                
                
            