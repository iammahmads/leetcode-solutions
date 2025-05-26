from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = list()
        def backtrack(open_count, closed_count, current):
            if len(current) == 2*n:
                result.append(current)
                return
            
            if open_count < n:
                backtrack(open_count + 1, closed_count, current + '(')
            if closed_count < open_count:
                backtrack(open_count, closed_count + 1, current + ')')
                
        backtrack(0, 0, "")
        return result
    
sol = Solution()
print(sol.generateParenthesis(1))
                
        
        