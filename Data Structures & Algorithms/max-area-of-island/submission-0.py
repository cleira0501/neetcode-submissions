class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        curr_area = 0

        def mark_island(i,j):
            nonlocal curr_area
            if i not in range(len(grid)) or j not in range(len(grid[0])) or not grid[i][j]:
                return
            #is "1"
            curr_area += 1
        
            grid[i][j] = 0
            mark_island(i+1, j)
            mark_island(i-1, j)
            mark_island(i, j+1)
            mark_island(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    mark_island(i,j)
                    if curr_area > max_area:
                        max_area = curr_area
                    curr_area = 0

        return max_area

        