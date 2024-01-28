#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
        xor_result = 0
        for num in nums:
            xor_result ^= num
    
        # Find the rightmost set bit in xor_result
        rightmost_set_bit = 1
        while (rightmost_set_bit & xor_result) == 0:
            rightmost_set_bit <<= 1
    
        # Initialize variables to store the two unique numbers
        num1 = 0
        num2 = 0
    
        # Partition the array based on the rightmost set bit
        for num in nums:
            if (num & rightmost_set_bit) == 0:
                num1 ^= num
            else:
                num2 ^= num
        
        return sorted([num2, num1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends