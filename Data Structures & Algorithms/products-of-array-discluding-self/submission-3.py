class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[1]*len(nums)
        prefix=1
        for i in range(1,len(nums)):
            prefix*=nums[i-1]
            arr[i]=prefix
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            arr[i]*=suffix
            suffix*=nums[i]
        return arr
