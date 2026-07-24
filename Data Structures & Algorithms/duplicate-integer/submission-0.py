class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            #if we havent seen it before, add it to the seen list
            if i in dict:
                return True
            else:
                dict[i] = 1
            #if we have seen it before, return true
        return False

        