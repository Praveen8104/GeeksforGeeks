#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        fib_sequence = [0, 1]
    
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
        return fib_sequence[:n] 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = Solution().fibonacciNumbers(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")

# } Driver Code Ends