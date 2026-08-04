class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False
        
        i = 0
        quota = 0
        while i < len(nums)-1:
            quota = max(quota,nums[i])
            if quota == 0:
                return False
            i +=1
            quota -=1 
        return True
        
        