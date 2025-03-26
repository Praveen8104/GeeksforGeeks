# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sum_index_map = {}  
        current_sum = 0
        max_length = 0
        for i in range(len(arr)):
            current_sum += arr[i]  
            if current_sum == k:
                max_length = i + 1 
            if (current_sum - k) in sum_index_map:
                max_length = max(max_length, i - sum_index_map[current_sum - k])
            if current_sum not in sum_index_map:
                sum_index_map[current_sum] = i
        return max_length



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends