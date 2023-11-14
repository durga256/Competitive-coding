class Solution:
    def dfs(self, grid, curr_x, curr_y):
        self.visited.add((curr_x, curr_y))
        for a,b in self.directions:
            next_x, next_y = curr_x+a, curr_y+b
            if 0 <= next_x <len(grid) and 0<= next_y <len(grid[0]) and grid[next_x][next_y] == '1' and (next_x, next_y) not in self.visited:
                self.dfs(grid,next_x, next_y) 

    def numIslands(self, grid) -> int:
        output = 0
        self.visited = set()
        self.directions = [[0,-1],[0,1],[1,0],[-1,0]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in self.visited:
                    output += 1
                    self.dfs(grid,i,j)

        return output
    
sol = Solution()
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]

print(sol.numIslands(grid))

