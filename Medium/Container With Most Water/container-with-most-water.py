#User function Template for python3



def maxArea(a,le):
    #code here
    left, right, max_area = 0, n - 1, 0

  # Loop through the array
    while left < right:
      # Calculate the area based on the minimum height of the two pointers
      current_area = min(a[left], a[right]) * (right - left)
      # Update the maximum area and pointers based on the current area
      max_area = max(max_area, current_area)
      if a[left] < a[right]:
        left += 1
      else:
        right -= 1
    return max_area

#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends