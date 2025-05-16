class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        result_dict = dict()
        for i in range(numRows):
            result_dict[i] = ""
        
        i = 0
        s_length = len(s)
        while i < s_length:
            for j in range(numRows):
                if(i >= s_length): break
                # print(i)
                result_dict[j] += s[i]
                i += 1

            iterator = numRows - 2
            while iterator > 0:
                if(i >= s_length): break
                print(i)
                result_dict[iterator] += s[i]
                iterator -= 1
                i += 1
            # print(result)
                
        
        result = ""
        for value in result_dict.values():
            result += value
        return result
        
sol = Solution()
print(sol.convert("PAYPALISHIRING", 4))