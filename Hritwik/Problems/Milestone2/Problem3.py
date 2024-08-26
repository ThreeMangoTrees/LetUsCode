import unittest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lenWord1, lenWord2 = len(word1), len(word2)
        i, j = 0, 0
        response_list = []
        while i<lenWord1 and j<lenWord2:
            response_list.append(word1[i])
            i+=1
            response_list.append(word2[j])
            j+=1

        if i==lenWord1 and j<lenWord2:
            for k in range(j, lenWord2):
                response_list.append(word2[k])

        if j==lenWord2 and i<lenWord1:
            for k in range(i, lenWord1):
                response_list.append(word1[k])

        response = ''.join(response_list)
        return response

class TestMergeAlternately(unittest.TestCase):

    def test_same_length(self):
        word1 = "abc"
        word2 = "def"
        expected = "adbecf"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_first_longer(self):
        word1 = "abcd"
        word2 = "xy"
        expected = "axbycd"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_second_longer(self):
        word1 = "ab"
        word2 = "xyz"
        expected = "axbyz"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_first_empty(self):
        word1 = ""
        word2 = "abc"
        expected = "abc"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_second_empty(self):
        word1 = "abc"
        word2 = ""
        expected = "abc"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_both_empty(self):
        word1 = ""
        word2 = ""
        expected = ""
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_special_characters(self):
        word1 = "a!@"
        word2 = "#$%"
        expected = "a#!$@%"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_single_characters(self):
        word1 = "a"
        word2 = "b"
        expected = "ab"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_long_strings(self):
        word1 = "abcdefghij"
        word2 = "klmnopqrst"
        expected = "akblcmdneofpgqhrisjt"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_mixed_case(self):
        word1 = "AbC"
        word2 = "xYz"
        expected = "AxbYCz"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

    def test_numeric_characters(self):
        word1 = "123"
        word2 = "456"
        expected = "142536"
        self.assertEqual(Solution().mergeAlternately(word1, word2), expected)

if __name__ == "__main__":
    unittest.main()
