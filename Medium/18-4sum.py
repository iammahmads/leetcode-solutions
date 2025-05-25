from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        result = set()
        for i in range(n):
            for j in range(i + 1, n):
                left, right = j+1, n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        
                        # skip duplicates from left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                            
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return [list(tup) for tup in result]
    
sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2], 0))
            