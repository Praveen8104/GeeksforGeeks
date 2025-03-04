//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
    public:
	int rec(int n){
	    int ans = n;
	    
	    if(n == 0) return 0;
	    
	    for(int i = 1; i <= sqrt(n); i++) {
	        int cnt = n/(i*i);
	        int temp = i*i;
	        cnt += rec(n%temp);
	        ans = min(ans,cnt);
	    }
	    return ans;
	}
    int MinSquares(int n) {
        // Code here
        return rec(n);
    }
};


//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int n;
        cin >> n;
        Solution ob;
        int ans = ob.MinSquares(n);
        cout << ans << "\n";
        cout << "~" << endl;
    }
    return 0;
}
// } Driver Code Ends