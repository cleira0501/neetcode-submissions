class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<4:
            return max(nums)
       
        rob1 = 0
        rob2 = 0
        rob3 = 0
        rob4 = 0
        for n in nums[:-1]:
            temp = rob2
            rob2 = max(rob1+n, temp)
            rob1 = temp
        for i in nums[1:]:
            temp = rob4
            rob4 = max(rob3+i, temp)
            rob3 = temp
        return max(rob2, rob4)