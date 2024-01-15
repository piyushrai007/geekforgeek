#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = set()  # Use a set for efficient membership checks
        stack = [0]
        ans = []
    
        while stack:
            p = stack.pop()
            if p not in visited:  # Check if already visited
                ans.append(p)
                visited.add(p)  # Mark as visited before processing neighbors
                for i in reversed(adj[p]):
                    stack.append(i)
    
        return ans
        

#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends