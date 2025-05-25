class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        result = True
        for i in range(len(s)):
            if len(stack) > 0 and (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                match s[i]:
                    case ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            result = False
                    
                    case '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            result = False
                    case ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            result = False
                    case _:
                        pass
            
            else:
                stack.append(s[i])
                
            if result == False:
                break
            
        if result == True:
            result = False if len(stack) > 0 else True
            
        print(stack)
        return result
    
    
sol = Solution()

print(sol.isValid("()[]{}["))