
class Solution:
    def minDeletion(self, s, k):
        from collections import Counter
        freq = Counter(s)
        frequencies = sorted(freq.values())

        if len(frequencies) <= k:
            return 0

        deletions = sum(frequencies[:len(frequencies) - k])
        return deletions
        
            
        
sol = Solution()
print(sol.minDeletion("yyyzz", 1))