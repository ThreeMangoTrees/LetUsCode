class Solution {
public:
    string convertToTitle(int columnNumber) {
        
        cout<<(columnNumber/26);
        string ans="";
        while(columnNumber)
        {
            columnNumber--;

            ans = ans+ char(columnNumber%26 + int('A'));
            columnNumber/=26;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};