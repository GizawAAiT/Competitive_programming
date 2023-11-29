class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        A=''
        unit={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
        ten={2:"Twenty",3:"Thirty",4:"Forty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
        
        teen={10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
        a={1:" Thousand",2:" Million",3:" Billion"}
        
        if len(str(num))==1: 
            A=unit[num]
        elif num<20:
            A=teen[num]  
        elif len(str(num))==2:
            A=ten[num/10] 
            if num%10!=0:
                A=A+" "+ unit[num%10]
        elif len(str(num))==3:
            A=unit[num/100] + " Hundred" 
            if num%100!=0:
                A= A +" "+ self.numberToWords( num%100)
        else:
            
            A=self.numberToWords( num%1000)
            num=num/1000
            i=0
            while num!=0:
                i+=1
                if A!="Zero" and num%1000:
                    
                    A= self.numberToWords(num%1000) + a[i] + " "+A
                elif num%1000:
                    A= self.numberToWords(num%1000)+ a[i] 
                num=num/1000
        return A
          
