#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        ans = []
        visited = set()  # Use a set to track visited nodes
        q = [0]  # Start from node 0
    
        while q:
            node = q.pop(0)  # Dequeue from the front
            if node not in visited:  # Check for duplicates before appending
                ans.append(node)
                visited.add(node)  # Mark node as visited
    
            for neighbor in adj[node]:
                if neighbor not in visited:
                    q.append(neighbor)
    
        return ans


        
            
            
            
            
            

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends