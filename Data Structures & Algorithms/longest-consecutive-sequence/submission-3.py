class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=sorted(nums)
        if not nums:
            return 0
        left,right=0,1
        maxi,count=1,1
        while right<len(nums):
            if arr[right]==arr[left]:
                right+=1
                continue
            elif arr[right]==arr[left]+1:
                count+=1
                maxi=max(maxi,count)
                left=right
                right+=1
            else:
                count=1
                left=right
                right+=1
            
        return maxi