class Solution {
public:
    vector<string> commonChars(vector<string>& words) {

        unordered_map<char,int> char_count;
        int len = words.size();

        for(string& str : words)
        {
            for(char& c : str)
            {
                if(char_count.find(c) == char_count.end())
                {
                    // not in hashmap
                    char_count[c]=1;
                    continue;
                }
                char_count[c]++;
            }
        }

        vector<string> ans;

        for(auto& i : char_count)
        {
            i.second = i.second/len;
        }
        
        for(auto& i : char_count)
        {
            if(i.second!=0)
            {   
                for(int j=0;j<i.second;j++)
                {
                    string a{i.first};
                    ans.push_back(a);
                }
            }
        }

        return ans;        
    }
};