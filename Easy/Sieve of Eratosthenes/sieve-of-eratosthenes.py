#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, n):
    	#code here 
        isPrime = [True] * (n + 1)
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(n**0.5) + 1):
          if isPrime[i]:
            for j in range(2 * i, n + 1, i):
              isPrime[j] = False
        ans = []
        for i in range(len(isPrime)):
            if isPrime[i]:
                ans.append(i)
        return ans
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends