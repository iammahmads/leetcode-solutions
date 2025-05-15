class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        result = []
        last_group = None
        
        for word, group in zip(words, groups):
            if group != last_group:
                result.append(word)
                last_group = group
        
        return result
        

sol = Solution()
print(sol.getLongestSubsequence(["d","a","v","b"], [1, 0,0,1]))