#User function Template for python3

class Solution:
    def leftRotate(self, arr, d):
        # code here
        n = len(arr)
        d = d % n
        arr[:] = arr[d:] + arr[:d]
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

        print("~")
# } Driver Code Ends