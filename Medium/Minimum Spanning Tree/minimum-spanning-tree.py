#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        pq = []
        vis = [0]*V
        sum = 0
        heapq.heappush(pq,(0,0))
        while pq:
            it = heapq.heappop(pq)
            node = it[1]
            wt  = it[0]
            if vis[node]==1:continue
            vis[node]=1
            sum+=wt
            for adjnode,ewt in adj[node]:
                if vis[adjnode]!=1:
                    heapq.heappush(pq,(ewt,adjnode))
        return sum
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends