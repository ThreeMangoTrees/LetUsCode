namespace VinitKumar.Problems.Milestone2
{
    public class Problem5 {
        public string LongestCommonPrefix(string[] strs) {
            string ans = "";

            for(int i=0;i<strs[0].Length;i++) {
                for(int j=1;j<strs.Length;j++) {
                    if(i >= strs[j].Length || strs[j][i] != strs[0][i]) {
                        return ans;
                    }
                }
                ans += strs[0][i];
            }
            return ans;
        }
    }
}