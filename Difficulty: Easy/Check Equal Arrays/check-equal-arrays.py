#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def checkEqual(self,A,B):
        
        #return: True or False
        
        #code here
        N = len(A)
        c=0
        A=sorted(A)
        B=sorted(B)
        for i in range(N):
                if A[i]==B[i]:
                    c+=1
        if c==N:
            return 1
        else:
            return 0




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tc in range(t):
        arr1 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        arr2 = [int(x) for x in input().replace('  ', ' ').strip().split(' ')]
        ob = Solution()
        if ob.checkEqual(arr1, arr2):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends