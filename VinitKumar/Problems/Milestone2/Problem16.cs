namespace VinitKumar.Problems.Milestone2
{
    public class Problem16 {
        public string AddStrings(string num1, string num2) {
            var total = "";
            var carry = 0;

            var ln1 = num1.Length - 1;
            var ln2 = num2.Length - 1;

            while(ln1 >= 0 || ln2 >= 0) {
                var sm = carry;
                if(ln1 >= 0) {
                    sm += int.Parse("" + num1[ln1]);
                }
                if(ln2 >= 0) {
                    sm += int.Parse("" + num2[ln2]);
                }

                total = (sm%10) + total;
                carry = sm/10;

                ln1--;
                ln2--;
            }

            if(carry > 0) {
                return carry + total;
            }

            return total;
        }
    }
}