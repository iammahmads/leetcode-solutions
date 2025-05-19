class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = str(x)
        j = len(s) - 1
        i = 0
        
        result = True
        while i <= j:
            if s[i] != s[j]:
                result = False
                break
            i += 1
            j -= 1
            
        return result
        
        
sol = Solution()
print(sol.isPalindrome(23232))