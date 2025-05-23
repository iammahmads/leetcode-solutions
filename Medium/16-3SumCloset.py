from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        closest_sum = float("inf")
        for i in range(n):
            left = i + 1
            right = n - 1
            
            while left < right:
                temp_sum = nums[i] + nums[left] + nums[right]
                
                if abs(temp_sum - target) < abs(closest_sum - target):
                    closest_sum = temp_sum
                    
                if temp_sum < target:
                    left += 1
                elif temp_sum > target:
                    right -= 1
                else:
                    return target
        return closest_sum
    
sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))