class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        dir = [
            [0,1],
            [-1,0],
            [1,0],
            [0, -1]
        ]
        def find_island(i, j):
            if i not in range(len(grid)) or j not in  range(len(grid[0])) or grid[i][j] == "0":
                return
            elif grid[i][j] == "1":
                grid[i][j] = "0"
            find_island(i+1,j)
            find_island(i,j+1)
            find_island(i-1,j)
            find_island(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                else:
                    island += 1
                    find_island(i,j)
        return island
    
                
   


                
        