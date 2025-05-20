from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        decrement_list = [0] * (n + 1)
        
        for start, end in queries:
            decrement_list[start] += 1
            decrement_list[end + 1] -= 1
            
        current_differnce = 0
        for i in range(n):
            current_differnce += decrement_list[i]
            if nums[i] > current_differnce:
                return False
        return True
            

sol = Solution()
print(sol.isZeroArray([2], [[0, 0],[0,0], [0, 0]]))