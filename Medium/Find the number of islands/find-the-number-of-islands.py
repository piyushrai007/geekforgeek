#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
from collections import deque

class Solution:
    def bfs(self, row, col, vis, grid):
        vis[row][col] = 1
        queue = deque([(row, col)])
        n, m = len(grid), len(grid[0])

        while queue:
            current_row, current_col = queue.popleft()

            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_row, new_col = current_row + i, current_col + j

                    if (
                        0 <= new_row < n
                        and 0 <= new_col < m
                        and grid[new_row][new_col] == 1
                        and vis[new_row][new_col] != 1
                    ):
                        vis[new_row][new_col] = 1
                        queue.append((new_row, new_col))

    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        count = 0

        for row in range(n):
            for col in range(m):
                if vis[row][col] == 0 and grid[row][col] == 1:
                    count += 1
                    self.bfs(row, col, vis, grid)

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends