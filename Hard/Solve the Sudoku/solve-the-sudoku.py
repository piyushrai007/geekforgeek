def is_safe(board, row, col, n, number):
    for i in range(n):
        if board[row][i] == number or board[i][col] == number:
            return False

    # for our grid
    stro = (row // 3) * 3
    stco = (col // 3) * 3

    for i in range(stro, stro + 3):
        for j in range(stco, stco + 3):
            if board[i][j] == number:
                return False

    return True


def help(board, row, col, n):
    if row == n:
        return True

    if col == n-1:
        nrow = row + 1
        ncol = 0
    else:
        nrow = row
        ncol = col + 1

    if board[row][col] != 0:
        return help(board, nrow, ncol, n)
    else:
        for i in range(1, 10):
            if is_safe(board, row, col, n, i):
                board[row][col] = i
                if help(board, nrow, ncol, n):
                    return True
                else:
                    board[row][col] = 0

    return False


class Solution:
    # Function to find a solved Sudoku.
    def SolveSudoku(self, grid):
        n = len(grid)
        return help(grid, 0, 0, n)

    # Function to print grids of the Sudoku.
    def printGrid(self, arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" ")

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends