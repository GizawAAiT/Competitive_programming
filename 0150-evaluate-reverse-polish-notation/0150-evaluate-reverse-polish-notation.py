class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        integer_stack = []
        for t in tokens:
            if t.isdigit(): 
                integer_stack.append(int(t)) 
                # print(integer_stack, t)
            elif len(t)>1 and t[0]=='-':
                integer_stack.append(-int(t[1:])) 
                # print(integer_stack, t)
            else:
                if t =="/":
                    if integer_stack[-1]*integer_stack[-2]<0:
                        integer_stack[-2] = ceil(integer_stack[-2] /integer_stack[-1])
                    else:
                        integer_stack[-2] //= integer_stack[-1] 
                    
                elif t == '*':
                    integer_stack[-2] *= integer_stack[-1]
                elif t == '-':
                    integer_stack[-2] -= integer_stack[-1]
                elif t == '+':
                    
                    integer_stack[-2] += integer_stack[-1] 
                integer_stack.pop()
                # print(integer_stack, t)
        return integer_stack[0]
                    