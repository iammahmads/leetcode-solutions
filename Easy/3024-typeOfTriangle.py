class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        def is_valid(points):
            return points[0] + points[1] > points[2] and points[1] + points[2] > points[0] and points[0] + points[2] > points[1] 
        
        
        if is_valid(nums):
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"
            elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
                return "isosceles"
            elif nums[0] != nums[1] != nums[2]:
                return "scalene"
            else:
                return "none"
        else:
            return "none"
        
        
sol = Solution()
print(sol.triangleType([3, 4, 5]))