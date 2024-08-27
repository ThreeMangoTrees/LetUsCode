namespace VinitKumar.Problems.Milestone2
{
    public class Problem13 {
        private bool HelperDict(string pattern, string s) {
            string[] sa = s.Split(' ');
            if(pattern.Length != sa.Length) {
                return false;
            }

            Dictionary<string, char> dict = new Dictionary<string, char>();
            Dictionary<char, string> dictC = new Dictionary<char, string>();
            for(int i=0;i<sa.Length;i++) {
                if(dict.ContainsKey(sa[i]) && dict[sa[i]] != pattern[i]) {
                    return false;
                } else if(!dict.ContainsKey(sa[i])) {
                    dict.Add(sa[i], pattern[i]);
                }

                if(dictC.ContainsKey(pattern[i]) && dictC[pattern[i]] != sa[i]) {
                    return false;
                } else if(!dictC.ContainsKey(pattern[i])) {
                    dictC.Add(pattern[i], sa[i]);
                }
            }

            return true;
        }

        public bool WordPattern(string pattern, string s) {
            return HelperDict(pattern, s);
        }
    }
}