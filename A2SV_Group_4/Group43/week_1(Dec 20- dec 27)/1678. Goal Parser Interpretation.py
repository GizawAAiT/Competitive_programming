class Solution:
    def interpret(self, command: str) -> str:
        output=[]
        for i in range(len(command)):
            if command[i]=="G": output.append("G")
            elif command[i]==")": output.append("al") if command[i-1] =="l" else output.append("o") 
        return "".join(output)