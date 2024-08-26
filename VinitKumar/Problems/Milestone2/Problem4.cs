namespace VinitKumar.Problems.Milestone2
{
    public class Problem4 {
        private string GetOnlyLetters(string s) {
            StringBuilder sb = new StringBuilder();
            foreach(char c in s) {
                if(Char.IsLetterOrDigit(c)) {
                    sb.Append(c);
                }
            }

            string ns = sb.ToString().ToLower();
            return ns;
        }

        private string GetOnlyLettersLINQ(string original) {
            string ans = new string(original.Where(c => char.IsLetterOrDigit(c)).ToArray());
            return ans.ToLower();
        }

        public bool IsPalindrome(string s) {
            //string ns = GetOnlyLetters(s);
            string ns = GetOnlyLettersLINQ(s);

            Console.WriteLine(ns);
            int nsl = ns.Length - 1;
            if(nsl == 0) {
                return true;
            }

            int i = 0;
            while(i < nsl) {
                if(ns[i] != ns[nsl]) {
                    return false;
                }
                i++;
                nsl--;
            }

            return true;
        }
    }
}