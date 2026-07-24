class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {key: [] for key in range(len(nums) + 1)}
        counts = Counter(nums)
        sol = []
        for num, freq in counts.items():
            count[freq].append(num)
        for i in reversed(range(1, len(nums) + 1)):
            if count[i]:
                sol.extend(count[i])
        return sol[:k]
