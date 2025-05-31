class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        n = len(needle)

        m = 0
        while m < len(haystack):
            if haystack[m] == needle[0]:
                index = m
                i = m + 1
                for j in range(1, n):
                    if i < len(haystack) and haystack[i] == needle[j]:
                        i += 1
                    else:
                        index = -1
                        break
            
            if index != -1:
                break
            m += 1
        return index
        


sol = Solution()
print(sol.strStr("assadbutsad", "sad"))