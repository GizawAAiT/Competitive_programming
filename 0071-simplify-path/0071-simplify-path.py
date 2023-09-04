class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        
        result_stack = []
        for p in path:
            if p == '..' and result_stack:
                result_stack.pop()
            elif p != '.' and p!='' and p!='..':
                result_stack.append(p)
        return '/'+'/'.join(result_stack)
