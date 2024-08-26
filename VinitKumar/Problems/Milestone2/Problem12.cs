
namespace VinitKumar.Problems.Milestone2
{
    public class Problem12 {
        private bool HelperDict(string s, string t) {
            Dictionary<char, int> dict = new Dictionary<char, int>();

            for(int i=0;i<s.Length;i++) {
                if(dict.ContainsKey(s[i])) {
                    dict[s[i]]++;
                } else if(!dict.ContainsKey(s[i])){
                    dict.Add(s[i],1);
                }


                if(dict.ContainsKey(t[i])) {
                    dict[t[i]]--;
                } else if(!dict.ContainsKey(t[i])) {
                    dict.Add(t[i], -1);
                }
            }

            foreach(var kvp in dict) {
                if(kvp.Value < 0 || kvp.Value > 0) {
                    return false;
                }
            }

            return true;
        }

        private bool HelperArray(string s, string t) {
            int[] arr = new int[26];
            for(int i=0;i<s.Length;i++) {
                arr[s[i] - 'a']++;
                arr[t[i] - 'a']--;
            }

            for(int i=0;i<26;i++) {
                if(arr[i] > 0 || arr[i] < 0) {
                    return false;
                }
            }

            return true;
        }

        public bool IsAnagram(string s, string t) {
            if(string.IsNullOrEmpty(s) && string.IsNullOrEmpty(t)) {
                return true;
            } else if(string.IsNullOrEmpty(s) || string.IsNullOrEmpty(t) || s.Length != t.Length) {
                return false;
            }
            // return HelperArray(s, t);
            return HelperDict(s, t);
        }
    }
}