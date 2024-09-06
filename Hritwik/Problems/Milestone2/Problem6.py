from collections import Counter
class Solution:
    def commonChars(self, words):
        common_chars = Counter(words[0])
        for word in words[1:]:
            word_chars = Counter(word)
            for char in common_chars:
                common_chars[char] = min(common_chars[char], word_chars.get(char,0)) 
        response = []
        for char, freq in common_chars.items():
            response.extend([char]*freq)
        return response

def test_case_1():
    solution = Solution()
    words = ["bella", "label", "roller"]
    expected_output = ['e', 'l', 'l']
    assert solution.commonChars(words) == expected_output, "Test Case 1 Failed!"
    print("Test Case 1 Passed!")

def test_case_2():
    solution = Solution()
    words = ["aaaa", "aaa", "aaaaa"]
    expected_output = ['a', 'a', 'a']
    assert solution.commonChars(words) == expected_output, "Test Case 2 Failed!"
    print("Test Case 2 Passed!")

def test_case_3():
    solution = Solution()
    words = ["abc", "def", "ghi"]
    expected_output = []
    assert solution.commonChars(words) == expected_output, "Test Case 3 Failed!"
    print("Test Case 3 Passed!")
if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()