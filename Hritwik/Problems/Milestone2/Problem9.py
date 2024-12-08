class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        response = []
        while columnNumber>0:
            columnNumber -= 1
            response.append(chr(columnNumber%26 + ord('A')))
            columnNumber = columnNumber//26
        return ''.join(response[::-1])

def test_case_1():
    solution = Solution()
    columnNumber = 1
    expected_output = "A"
    assert solution.convertToTitle(columnNumber) == expected_output, "Test Case 1 Failed!"
    print("Test Case 1 Passed!")

def test_case_2():
    solution = Solution()
    columnNumber = 28
    expected_output = "AB"
    assert solution.convertToTitle(columnNumber) == expected_output, "Test Case 2 Failed!"
    print("Test Case 2 Passed!")

def test_case_3():
    solution = Solution()
    columnNumber = 701
    expected_output = "ZY"
    assert solution.convertToTitle(columnNumber) == expected_output, "Test Case 3 Failed!"
    print("Test Case 3 Passed!")    

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
