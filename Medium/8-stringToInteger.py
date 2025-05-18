class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
            
        result = ""
        for i in range(len(s)):
            if s[i] not in NUMBERS:
                break
            result += s[i]
        
        if not result:
            return 0
        
        result = int(result) * sign
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        return result
    
sol = Solution()
print(sol.myAtoi("-91283472332"))