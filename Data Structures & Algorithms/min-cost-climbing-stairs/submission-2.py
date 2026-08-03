class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<2:
            return 0
        elif len(cost) ==2:
            return min(cost)
        cost1, cost2 = 0,0
        cost.append(0)
        cost.append(0)
        for i in range(2, len(cost)):
            temp = cost2
            cost2 = min(cost1 + cost[i-2], cost2 +cost[i-1])
            cost1 = temp
        return min(cost1, cost2)


        