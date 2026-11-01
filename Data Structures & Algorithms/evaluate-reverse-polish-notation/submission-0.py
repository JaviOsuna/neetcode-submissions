class Solution:
    def doOperation(self, operator: str, a: int, b: int) -> int:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a*b
        elif operator == '/':
            return a/b

    def evalRPN(self, tokens: List[str]) -> int:
        result = [] # stack
        for t in tokens:
            if t in '+-*/':
                value1 = result.pop()
                value2 = result.pop()
                result.append(int(self.doOperation(t, value2, value1)))
            else:
                result.append(int(t))
        return result[0]