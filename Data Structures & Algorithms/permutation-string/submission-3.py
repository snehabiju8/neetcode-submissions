class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ch={}
        ch1={}
        n=len(s1)
        m=len(s2)
        if n>m:
            return False
        for i in range(n):
            if s1[i] not in ch:
                ch[s1[i]]=1
            else:
                ch[s1[i]]+=1
        for i in range(n):
            if s2[i] not in ch1:
                ch1[s2[i]]=1
            else:
                ch1[s2[i]]+=1
        if ch1==ch:
            return True
        for i in range(n,m):
            right=i
            left=i-n
            if s2[right] not in ch1:
                ch1[s2[right]]=1
            else:
                ch1[s2[right]]+=1      
            ch1[s2[left]]-=1
            if ch1[s2[left]] == 0:
                del ch1[s2[left]]
            if ch1==ch:
                return True
        return False