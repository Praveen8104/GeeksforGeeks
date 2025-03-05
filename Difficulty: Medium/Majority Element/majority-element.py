#User function template for Python 3

class Solution:
    def majorityElement(self, A):
        #Your code here
        N = len(A)
        n=N//2
        d={}
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=[]
        for i in d.keys():
            if d[i]>n:
                c.append(i)
        if len(c)==0:
            return -1
        for i in c:
            return i

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends