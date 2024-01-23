
class Solution:

    def is_safe(self, r, c, board):
        n = len(board)

        # Check left col
        for i in range(c):
            if board[r][i]:
                return False

        # Check left-up diagonal
        i, j = r, c
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i, j = i - 1, j - 1

        # Check left-down diagonal
        i, j = r, c
        while i < n and j >= 0:
            if board[i][j]:
                return False
            i, j = i + 1, j - 1

        return True

    def nQueen(self, n):
        board = [[0 for _ in range(n)] for _ in range(n)]
        buf = []
        result = []

        def rec(c):
            nonlocal buf, result, board
            if c >= n:
                return True

            for r in range(n):
                if self.is_safe(r, c, board):
                    board[r][c] = 1
                    buf.append(r+1)

                    if rec(c + 1):
                        result.append([x for x in buf])

                    buf.pop()
                    board[r][c] = 0

            return False

        rec(0)
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends