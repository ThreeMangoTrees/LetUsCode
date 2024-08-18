from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        def find_first_prefix(word1, word2):
            ptr_wrd1, ptr_wrd2 = 0,0
            response = []
            while ptr_wrd1<len(word1) and ptr_wrd2<len(word2):
                if word1[ptr_wrd1]==word2[ptr_wrd2]:
                # print(f'Before: ptr_wrd1 = {ptr_wrd1}, ptr_wrd2 = {ptr_wrd2}, common weord = {word1[ptr_wrd1]}')
                    response.append(word1[ptr_wrd1])
                    ptr_wrd1+=1
                    ptr_wrd2+=1
                else:
                    break
                # print(f'After: ptr_wrd1 = {ptr_wrd1}, ptr_wrd2 = {ptr_wrd2}, response = {response}')
            return ''.join(response)
        first_common = strs[0]
        for word in strs[1:]:
            first_common = find_first_prefix(first_common,word)
            if not first_common:
                break
        return first_common

# Test Case 1: Common Prefix Exists
def test_case_1():
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    expected_output = "fl"
    assert solution.longestCommonPrefix(strs) == expected_output, f"Expected {expected_output}, but got {solution.longestCommonPrefix(strs)}"
    print("Test Case 1 Passed")

# Test Case 2: No Common Prefix
def test_case_2():
    solution = Solution()
    strs = ["dog", "racecar", "car"]
    expected_output = ""
    assert solution.longestCommonPrefix(strs) == expected_output, f"Expected {expected_output}, but got {solution.longestCommonPrefix(strs)}"
    print("Test Case 2 Passed")

if __name__ == "__main__":
    test_case_1()
    test_case_2()