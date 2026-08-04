class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        new_list = [x - y for x, y in zip(gas, cost)]
        if sum(new_list) < 0:
            return -1
        start = 0
        curr_tank = 0
        for i in range(len(new_list)):
            curr_tank += new_list[i]
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        return start

        