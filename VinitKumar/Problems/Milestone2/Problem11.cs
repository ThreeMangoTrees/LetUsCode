namespace VinitKumar.Problems.Milestone2
{
    public class Problem11 {
        private bool IsIsomorphicUsingDict(string s, string t) {
                
            Dictionary<char, int> dict = new Dictionary<char, int>();
            Dictionary<char, int> dictS = new Dictionary<char, int>();

            for(int i=0;i<s.Length;i++) {
                if(dict.ContainsKey(t[i]) && dict[t[i]] != s[i]) {
                    return false;
                }
                if(dictS.ContainsKey(s[i]) && dictS[s[i]] != t[i]) {
                    return false;
                }
                dict[t[i]] = s[i];
                dictS[s[i]] = t[i];
            } 
            return true;
        }

        public bool IsIsomorphic(string s, string t) {
            if(s.Length != t.Length) {
                return false;
            }

            return IsIsomorphicUsingDict(s,t);
        }
    }
}