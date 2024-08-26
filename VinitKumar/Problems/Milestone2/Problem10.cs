namespace VinitKumar.Problems.Milestone2
{
    public class Problem10 {
        public int TitleToNumber(string columnTitle) {
            int ans = 0;
            for(int i=0;i<columnTitle.Length;i++) {
                char ascii = columnTitle[i];
                int val = ascii - 'A' + 1;
                ans = ans * 26 + val;
            }
            return ans;
        }
    }
}