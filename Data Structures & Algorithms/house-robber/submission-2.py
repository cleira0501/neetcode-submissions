class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        rob1 = nums[0]
        rob2 = max(nums[0],nums[1])
        for n in nums[2:]:
            temp = rob2
            rob2 = max(n + rob1, rob2)
            rob1 = temp
        return rob2