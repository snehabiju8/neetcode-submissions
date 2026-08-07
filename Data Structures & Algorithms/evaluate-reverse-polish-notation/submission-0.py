class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ch in tokens:
            if ch not in "+-/*":
                stack.append(int(ch))
            else:
                if ch=="+":
                    b=stack.pop()
                    a=stack.pop()
                    c=b+a
                    stack.append(c)
                elif ch=="-":
                    b=stack.pop()
                    a=stack.pop()
                    c=a-b
                    stack.append(c)
                elif ch=="*":
                    b=stack.pop()
                    a=stack.pop()
                    c=a*b
                    stack.append(c)
                elif ch=="/":
                    b=stack.pop()
                    a=stack.pop()
                    c=int(a/b)
                    stack.append(c)
        return stack.pop()