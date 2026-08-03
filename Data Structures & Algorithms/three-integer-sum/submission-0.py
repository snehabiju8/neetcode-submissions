class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            target=-nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                curr=nums[left]+nums[right]
                if curr==target:
                    res=[nums[i],nums[left],nums[right]]
                    if res not in ans:
                        ans.append(res) 
                    left+=1
                    right-=1
                elif curr<target:
                    left+=1
                else:
                    right-=1
        return ans