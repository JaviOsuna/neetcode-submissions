class Solution:

 

    def isValid(self, s: str) -> bool:
        check = {
            ')' : '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for w in s:
            if w in check.values():
                stack.append(w)
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if check[w] != top:
                    return False
        return len(stack) == 0 


           
            
