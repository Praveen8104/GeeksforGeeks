//{ Driver Code Starts
#include <iostream>
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution{
    public:
    string solve (int k, string &s,int c){
        int n=s.size();
        if( c==-1 || s.size()==0 ){
            return s;
        }
        int f=k;
        int i=0,j=0,h=1;
        while(i<s.size()-1){
            if (s[i]==s[i+1]){
                i+=1;
                h+=1;
                if (h==f){
                    j=i-k+1;
                    s.erase(j,f);
                    h=1;
                }
            }
            else{
                i+=1;
                h=1;
            }
        }
        if (s.size()==n){
            c=-1;
        }
        return solve( k,s, c);
    }
    string Reduced_String(int k,string s){
        // Your code goes here
        int c=0;
        if(k==1){
            return "";
        }
        if (s.size()==1){
            return s;
        }
        string su=solve(k,s,c);
        return su;
    }
};




//{ Driver Code Starts.

int main() {
    
    
    int t;cin>>t;
    while(t--)
    {
        int k;
        cin>>k;
        string s;
        cin>>s;
        Solution obj;
        cout<<obj.Reduced_String(k,s)<<"\n";
        
    
cout << "~" << "\n";
}
    
	return 0;
}
// } Driver Code Ends