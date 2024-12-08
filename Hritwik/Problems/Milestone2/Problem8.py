
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        response = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                response.append("FizzBuzz")
            elif i%3 == 0:
                response.append("Fizz")
            elif i%5 == 0:
                response.append("Buzz")
            else:
                response.append(f"{i}")
        return response

def test_case_1():
    solution = Solution()
    n = 3
    expected_output = ["1","2","Fizz"]
    assert solution.fizzBuzz(n) == expected_output, "Test Case 1 Failed!"
    print("Test Case 1 Passed!")

def test_case_2():
    solution = Solution()
    n = 5
    expected_output = ["1","2","Fizz","4","Buzz"]
    assert solution.fizzBuzz(n) == expected_output, "Test Case 2 Failed!"
    print("Test Case 2 Passed!")

def test_case_3():
    solution = Solution()
    n = 15
    expected_output = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    assert solution.fizzBuzz(n) == expected_output, "Test Case 3 Failed!"
    print("Test Case 3 Passed!")    

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
