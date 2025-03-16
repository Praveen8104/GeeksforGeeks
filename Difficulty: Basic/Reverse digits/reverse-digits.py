#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
        reversed_number = 0
        while n > 0:
            last_digit = n % 10
            reversed_number = reversed_number * 10 + last_digit
            n //= 10
    
        return reversed_number

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.reverseDigits(n)
        print(ans)

        print("~")

# } Driver Code Ends