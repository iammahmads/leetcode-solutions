from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers_list = {
            2: ('a', 'b', 'c'),
            3: ('d', 'e', 'f'),
            4: ('g', 'h', 'i'),
            5: ('j', 'k', 'l'),
            6: ('m', 'n', 'o'),
            7: ('p', 'q', 'r', 's'),
            8: ('t', 'u', 'v'),
            9: ('w', 'x', 'y', 'z'),
        }
        
        result = []
        
        def backtrack(index, current, total_length):
            
            if index == total_length:
                result.append("".join(current))
                return
                
            for letter in numbers_list[int(digits[index])]:
                current.append(letter)
                backtrack(index + 1, current, total_length)
                current.pop()
            
        n = len(digits)
        if n == 0:
            return result
        backtrack(0, [], n)
        return result

sol = Solution()
print(sol.letterCombinations("23"))