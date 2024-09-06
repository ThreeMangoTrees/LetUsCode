class Solution:
    def romanToInt(self, s: str) -> int:
        record={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        sz_s=len(s)
        i=0
        while i < sz_s:

            if i+1<sz_s and s[i]=='I' and s[i+1]=='V':
                sum=sum+4
                i+=2
            elif i+1<sz_s and s[i]=='I' and s[i+1]=='X':
                sum=sum+9
                i+=2
            elif i+1<sz_s and s[i]=='X' and s[i+1]=='L':
                sum=sum+40
                i+=2
            elif i+1<sz_s and s[i]=='X' and s[i+1]=='C':
                sum=sum+90
                i+=2
            elif i+1<sz_s and s[i]=='C' and s[i+1]=='D':
                sum+=400
                i+=2
            elif i+1<sz_s and s[i]=='C' and s[i+1]=='M':
                sum=sum+900
                i+=2
            else:
                sum=sum+record[s[i]]
                i+=1
                    
        return sum
    
def test_case_1():
    solution = Solution()
    s = "III"
    expected_output = 3
    assert solution.romanToInt(s) == expected_output, "Test Case 1 Failed!"
    print("Test Case 1 Passed!")

def test_case_2():
    solution = Solution()
    s = "LVIII"
    expected_output = 58
    assert solution.romanToInt(s) == expected_output, "Test Case 2 Failed!"
    print("Test Case 2 Passed!")

def test_case_3():
    solution = Solution()
    s = "MCMXCIV"
    expected_output = 1994
    assert solution.romanToInt(s) == expected_output, "Test Case 3 Failed!"
    print("Test Case 3 Passed!")    

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
