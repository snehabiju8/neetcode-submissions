class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(0,n):
                if(nums[i] + nums[j] == target and i!=j):
                    out.append(i)
                    out.append(j)
                    return out
        
