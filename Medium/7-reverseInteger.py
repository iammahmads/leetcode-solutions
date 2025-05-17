class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31-1
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        x = str(x)[::-1]
        x = int(x)
        
        if x < INT_MIN or x > INT_MAX:
            return 0
        return x if sign == 1 else sign * x
        
sol = Solution()
print(sol.reverse(-123))