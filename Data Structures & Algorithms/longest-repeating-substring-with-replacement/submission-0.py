class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        left=0
        right=0
        max_freq=0
        best=0
        while right<len(s):
            ch=s[right]
            if ch not in counts:
                counts[ch]=1
            else:
                counts[ch]+=1
            max_freq=max(max_freq,counts[ch])
            while (right-left+1)-max_freq>k:
                counts[s[left]]-=1
                left+=1
            best=max(best,right-left+1)
            right+=1
        return best

        