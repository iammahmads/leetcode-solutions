from typing import List

class Solution:
    def maxArea(self, height: List[int])->int:
        left = 0
        right = len(height) - 1
        max_liters = 0
        
        while left < right:
            new_candiate_value = min(height[left], height[right]) * (right - left)
            if max_liters < new_candiate_value:
                    max_liters = new_candiate_value 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                                        
        return max_liters
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))