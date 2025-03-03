#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, K):
        #Your code here
        i = 0
        j = len(arr)-1
        while (1):
            mid = (i+j)//2
            if arr[mid] == K:
                return True
            elif arr[mid]>K:
                j=mid-1
            elif arr[mid] < K:
                i=mid+1
            if i>j:
                return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print("true" if ob.searchInSorted(A, k) else "false")
        print("~")

# } Driver Code Ends