#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        ans = 0
        for i in range(1,n+1):
            ans += (i**3)
            
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
        print("~")
# } Driver Code Ends