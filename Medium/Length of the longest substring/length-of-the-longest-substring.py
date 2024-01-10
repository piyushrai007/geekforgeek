#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        dict = {s[i]:-1 for i in range(0,len(s))}

        maxline = 0
        start =-1
        for i in range(0,len(s)):
            if dict[s[i]]>start:
                start = dict[s[i]]
            dict[s[i]] = i
            maxline = max(maxline,i-start)
        return maxline


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends