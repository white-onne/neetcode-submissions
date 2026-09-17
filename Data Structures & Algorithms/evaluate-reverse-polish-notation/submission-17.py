class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for tk in tokens:
            if tk.isdigit() or (len(tk)>1 and tk[0] == "-"):
                stack.append(int(tk))
            elif tk == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a+b)
            elif tk == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif tk == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a*b)
            elif tk == "/":
                b = stack.pop()
                a = stack.pop()
                if a == 0:
                    stack.append(0)
                else: stack.append(int(a/b))
        return stack[-1]