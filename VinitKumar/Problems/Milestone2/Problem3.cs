namespace VinitKumar.Problems.Milestone2
{
    public class Problem3 {
        public string MergeAlternately(string word1, string word2) {
            string ans = "";
            if(word1.Length >= word2.Length) {
                for(int i = 0;i < word1.Length;i++) {
                    ans = ans + word1[i];
                    if(i < word2.Length) {
                        ans = ans + word2[i];
                    }
                }
            } else {
                for(int i = 0;i < word2.Length;i++) {
                    if(i < word1.Length) {
                        ans = ans + word1[i];
                    }
                    ans = ans + word2[i];
                }
            }
            return ans;
        }
    }
}