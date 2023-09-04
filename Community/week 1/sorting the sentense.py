class Solution:
    def sortSentence(self, s):
        list = ()

        l=s.split(" ")
        answer = ""
        for i in range(len(l)):
            for j in l:
                if int(j[-1]) == (i+1):
                    answer +=j[:-1]
                    answer +=(" ")
        return (answer[:-1])
