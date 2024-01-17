import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        min_heap = []
        
        dist = [10000000000]*V
        dist[S]=0
        heapq.heappush(min_heap,(0,S))

        while min_heap:
            a= heapq.heappop(min_heap)
            dis = a[0]
            node = a[1]
            for adjnode, weight in adj[node]:  # Unpack directly
                if dis + weight < dist[adjnode]:
                    dist[adjnode] = dis + weight
                    heapq.heappush(min_heap, (dist[adjnode], adjnode))
            
        return dist
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends