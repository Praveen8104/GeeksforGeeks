#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3


class Solution:
    def sumExceptFirstLast(self,arr):
        # Parr:  list of pair
        #code here
        if len(arr) < 3:
            return 0
        
        return sum(arr[1:-1])

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.sumExceptFirstLast(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends