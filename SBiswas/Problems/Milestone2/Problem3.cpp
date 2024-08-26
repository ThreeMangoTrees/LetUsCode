class Solution {
public:
    string mergeAlternately(string word1, string word2) {

        int word1_size = word1.length();
        int word2_size = word2.length();

        int i=0, j=0;
        bool flag=true;
        string ans="";

        while(i<word1_size || j<word2_size)
        {
            if(i>=word1_size)
            {
                // word1 has finised
                ans = ans + word2.substr(j,word2_size-j);
                break;
            }

            if(j>=word2_size)
            {
                // word1 has finised
                ans = ans + word1.substr(i,word1_size-i);
                break;
            }
            
            if(flag)
            {
                ans+=word1[i];
                i++;
            }
            else
            {
                ans+=word2[j];
                j++;
            }

            flag = flag^true;


        }

        return ans;
        
    }
};