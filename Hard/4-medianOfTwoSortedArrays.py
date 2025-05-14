class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums = sorted(nums1 + nums2)
        nums_length = len(nums)       
        
        if nums_length % 2 == 0:
            return (nums[(nums_length // 2) - 1] + nums[nums_length // 2]) / 2.0
        
        return nums[nums_length // 2]
        
        
        
nums1 = [1, 2]
nums2 = [3, 4]
sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))