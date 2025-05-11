class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        consective_odds = 0
        for i in range(len(arr)):
            if(arr[i] % 2 != 0):
                consective_odds = consective_odds + 1
                if consective_odds == 3:
                    return True
            else:
                consective_odds = 0
        return False
    
sol = Solution()
print(sol.threeConsecutiveOdds([1, 4, 5, 8, 9]))