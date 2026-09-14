class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        operands = ['+','-','*','/']
        for token in tokens:
            
            if token in operands:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    tmp = a+b
                elif token == '-':
                    tmp = a-b
                elif token == '*':
                    tmp = a*b
                elif token == '/':
                    tmp = a/b
            else:
                tmp = token
            stack.append(int(tmp))
            #print(stack)
        ans = stack[0]
        return ans
                