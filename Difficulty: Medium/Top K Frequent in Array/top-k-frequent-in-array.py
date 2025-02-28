#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import deque

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# } Driver Code Ends

class Solution:
	def topKFrequent(self, nums, k):
		# your code here
		d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        d = dict(sorted(d.items(), key=lambda item: (item[1],item[0]), reverse=True))
        l = []
        cnt = 0
        for i in d.keys():
            if cnt == k:
                break
            l.append(i)
            cnt += 1
        return l
		


#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.topKFrequent(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")

# } Driver Code Ends