class Solution:
    def findMedian(self, arr):
        #code here.
        arr.sort()
        n = len(arr)
        if n % 2 != 0:
            return arr[n // 2]
        else:
            mid1 = arr[n // 2 - 1]
            mid2 = arr[n // 2]
            return (mid1 + mid2) / 2
#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Reading the number of test cases
    for _ in range(t):
        arr = list(map(int,
                       input().strip().split())
                   )  # Reading and converting input to a list of integers
        solution = Solution()
        ans = solution.findMedian(
            arr)  # Calling the function and printing the result
        if int(ans) == ans:
            print(int(ans))
        else:
            print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends