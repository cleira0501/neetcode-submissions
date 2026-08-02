import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = [-x for x in stones]
        heapq.heapify(stone_heap)
        def recurse(max_heap):
            if len(max_heap) == 0:
                return 0
            elif len(max_heap) == 1:
                return -max_heap[0]
            
            remain = heapq.heappop(max_heap) - heapq.heappop(max_heap)
            if remain:
                heapq.heappush(max_heap, remain)
            
            return recurse(max_heap)

        return recurse(stone_heap)

        