class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower=s.lower()
        string=""
        for i in lower:
            if i.isalnum():
                string=string+i
        if string==string[::-1]:
            return True
        else:
            return False