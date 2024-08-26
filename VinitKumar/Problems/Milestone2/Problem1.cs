
namespace VinitKumar.Problems.Milestone2
{
    public class Problem1 {
        public bool ValidWordAbbreviation(string word, string abbr) {
            if(abbr.Length > word.Length) {
                return false;
            }
            int wi = 0;
            string  n = "";
            for(int wa = 0; wa < abbr.Length; wa++) {
                if(char.IsDigit(abbr[wa])) {
                    n = n + abbr[wa];
                    continue;
                }

                if(n.Length > 0) {
                    if(n[0] == '0') {
                        return false;
                    }
                    wi += Int32.Parse(n);
                    n = "";
                }

                if(wi >= word.Length) {
                    return false;
                }

                if(abbr[wa] == word[wi]) {
                    wi++;
                } else {
                    return false;
                }
            }

            if(n.Length > 0) {
                if(n[0] == '0') {
                    return false;
                }
                wi += Int32.Parse(n);
            }

            return wi == word.Length ? true : false;
        }
    }
}