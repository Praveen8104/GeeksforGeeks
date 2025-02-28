#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        pre = [1] * n
        suff = [1] * n
        res = [0] * n
        
        for i in range(1,n):
            pre[i] = pre[i-1] * arr[i-1]
            
        for i in range(n-2,-1,-1):
            suff[i] = suff[i+1] * arr[i+1]
        
        for i in range(n):
            res[i]  = pre[i] * suff[i]
        
        return res




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends