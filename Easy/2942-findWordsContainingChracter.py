from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[str]:
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
        
        return result
    
sol = Solution()
print(sol.findWordsContaining(["leet","code"], "e"))