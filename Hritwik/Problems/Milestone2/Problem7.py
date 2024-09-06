class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for char_s, char_t in zip(s, t):
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False     
            else:
                s_to_t[char_s] = char_t
            
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
        return True 
def test_case_1():
    solution = Solution()
    s = "egg"
    t = "add"
    expected_output = True
    assert solution.isIsomorphic(s, t) == expected_output, "Test Case 1 Failed!"
    print("Test Case 1 Passed!")

def test_case_2():
    solution = Solution()
    s = "foo"
    t = "bar"
    expected_output = False
    assert solution.isIsomorphic(s, t) == expected_output, "Test Case 2 Failed!"
    print("Test Case 2 Passed!")

if __name__ == "__main__":
    test_case_1()
    test_case_2()
