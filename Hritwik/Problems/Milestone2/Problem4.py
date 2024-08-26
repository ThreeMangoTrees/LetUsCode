class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=[]
        for char in list(s):
            if char.isalpha() or char.isdigit():
                word.append(char.lower())
        word=''.join(word)
        start, end = 0, len(word)-1
        while start<end:
            if word[start]!=word[end]:
                return False
            else:
                start+=1
                end-=1

        return True

import unittest
class TestMergeAlternately(unittest.TestCase):

    def test_even_length(self):
        word = "adbecf"
        expected = False
        self.assertEqual(Solution().isPalindrome(word), expected)

    def test_odd_length(self):
        word = "abcde"
        expected = False
        self.assertEqual(Solution().isPalindrome(word), expected)

    def test_odd_length_upper_case_and_lower_case(self):
        word = "As5dbd5sA"
        expected = True
        self.assertEqual(Solution().isPalindrome(word), expected)
    
    def test_longer(self):
        word = "race a car"
        expected = False
        self.assertEqual(Solution().isPalindrome(word), expected)

    def test_sentense(self):
        word = "A man, a plan, a canal: Panama"
        expected = True
        self.assertEqual(Solution().isPalindrome(word), expected)
    
    def test_empty(self):
        word = " "
        expected = True
        self.assertEqual(Solution().isPalindrome(word), expected)


if __name__ == "__main__":
    unittest.main()
