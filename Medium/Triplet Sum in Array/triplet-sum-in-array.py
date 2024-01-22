#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here
        arr = sorted(A)

        # Iterate through the array
        for i in range(n):
            # Set two pointers, one at the beginning of the remaining sub-array and one at the end
            left = i + 1
            right = n - 1

            # Find the two elements that sum to the negative of the current element
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                if current_sum == X:
                    # Found a triplet
                    return True
                elif current_sum < X:
                    # Need a larger element from the right
                    left += 1
                else:
                    # Need a smaller element from the left
                    right -= 1

        # No triplet found
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends