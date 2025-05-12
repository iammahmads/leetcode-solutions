class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        from itertools import permutations
        result = set()
        
        for perm in permutations(digits, 3):
            if perm[0] == 0: continue
            if perm[2] % 2 != 0: continue
            result.add(perm[0] * 100 +  perm[1] * 10 + perm[2])
            
        return sorted(result)
        
sol = Solution()
sol.findEvenNumbers([2, 1, 3, 0])