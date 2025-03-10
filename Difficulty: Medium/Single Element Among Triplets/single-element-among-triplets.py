#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        one, two = 0, 0
        for i in arr:
            one = (one ^ i) & ~ two
            two = (two ^ i) & ~ one
        return one

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
        print("~")
# } Driver Code Ends