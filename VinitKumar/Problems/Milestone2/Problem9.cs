namespace VinitKumar.Problems.Milestone2
{
    public class Problem9 {
        private Tuple<int, int> Helper(int num) {
            int div = num / 26;
            int md = num % 26;
            return new Tuple<int,int>(div, md);
        }
        public string ConvertToTitle(int columnNumber) {
            string ans = "";
            while(columnNumber > 26) {
                (columnNumber, int md) = Helper(columnNumber);
                if(md == 0 && columnNumber > 0) {
                    columnNumber -= 1;
                    md = 26;
                }

                ans = md > 0 ? ((char)('A' + (md - 1))).ToString() + ans : ans;  
            }

            ans = columnNumber > 0 ? ((char)('A' + (columnNumber - 1))).ToString() + ans : ans;
            return ans;
            
        }
    }
}