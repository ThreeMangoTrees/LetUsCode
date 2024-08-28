namespace VinitKumar.Problems.Milestone2
{
    public class Problem15 {
        public int LengthOfLastWord(string s) {
            s = s.Trim();
            string[] words = s.Split(' ');
            return words[words.Length - 1].Length;
        }
    }
}