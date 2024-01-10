#User function Template for python3

# arr[] : int input array of integers
# k : the quadruple sum required
class Solution:
    def fourSum(self, nums, target):
        # code here
        n = len(nums) # size of the array
        ans = []
    
        # sort the given array:
        nums.sort()
    
        # calculating the quadruplets:
        for i in range(n):
            # avoid the duplicates while moving i:
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # avoid the duplicates while moving j:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
    
                # 2 pointers:
                k = j + 1
                l = n - 1
                while k < l:
                    _sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if _sum == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)
                        k += 1
                        l -= 1
    
                        # skip the duplicates:
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif _sum < target:
                        k += 1
                    else:
                        l -= 1
    
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Main
if __name__=='__main__':
    t = int(input())
    while t:
        t-=1
        n, k=map(int,input().split())
        # print(n, k)
        a=list(map(int,input().strip().split()))[:n]
        # print(a)
        ob=Solution()
        ans=ob.fourSum(a, k)
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print("$", end="")
        if(len(ans)==0):
            print(-1, end="")
        print()
        
        

# } Driver Code Ends