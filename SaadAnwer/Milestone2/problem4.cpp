class Solution {
public:
    bool isPalindrome(string s) {
        string res = "";
        for(auto ch: s) 
        {
        if((ch>='A'&&ch<='Z')||(ch>='a'&&ch<='z')||(ch>='0'&&ch<='9')) {
            if(ch>='0'&&ch<='9') res.push_back(ch);
            else res.push_back((ch>'Z'? ch : ch+32));
            }
        }
         int l =0;
        int r= res.size()-1;
        while(l<r) if(res[l++]!=res[r--]) return false;
        return true;
        
    }
};