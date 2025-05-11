class Solution(object):
    def twoSum(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(arr):
            complement = target - num #  => 6-3 = 3
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return[]

sol = Solution()
print(sol.twoSum([3, 2, 4], 6))                