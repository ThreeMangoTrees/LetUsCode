class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_map={}
        hash_map['[']=']'
        hash_map['{']='}'
        hash_map['(']=')'
        print(hash_map)
        for bracket in s:
            if len(stack)==0 and (bracket == ']'or bracket == '}' or bracket == ')'):
                return False
            elif bracket == '['or bracket == '{' or bracket == '(':
                print(f'Append: {bracket} to stack')
                stack.append(bracket)
            elif len(stack)!=0 and (bracket == ']'or bracket == '}' or bracket == ')'):
                print(f'Print stack[-1] : {stack[-1]}')
                if hash_map[stack[-1]]==bracket:
                    print(f'Check if {stack[-1]} is equal to {bracket} and is valid for pop()')
                    stack.pop()
                else:
                    print(f'invalid parenthesis due to closing bracket')
                    return False
        if len(stack)==0:
            return True
