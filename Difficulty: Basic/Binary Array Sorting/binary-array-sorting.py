
class Solution:
    # Function to sort the binary array in non-decreasing order
    def binSort(self, arr):
        # code here
        arr = arr.sort()
        return arr



#{ 
 # Driver Code Starts
# Driver code
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    Solution().binSort(arr)  # sort the binary array

    print(*arr)  # print the sorted array
    print("~")

# } Driver Code Ends