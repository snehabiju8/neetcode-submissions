class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in s:
            if i not in brackets:
                stack.append(i)
            else:
                if not stack or stack[-1]!=brackets[i]:
                    return False
                stack.pop()
        return len(stack)==0
        