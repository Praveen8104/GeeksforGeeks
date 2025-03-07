#User function Template for python3


class Solution:
    def factorial (self, n):
        # code here
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

        print("~")

# } Driver Code Ends