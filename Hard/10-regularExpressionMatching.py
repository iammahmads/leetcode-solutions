# Attempted But not Solved
# The Solution is invalid










# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         s_len = len(s)
#         p_len = len(p)
        
#         i = j = k = 0
#         max_len = max(s_len, p_len)
#         result = True
#         while k < max_len:
#             print(i, s_len)
#             print(j, p_len)
            
#             if k >= i or k >= j:
#                 if s_len != p_len:
#                     result = False
            
#             if s[i] == p[j]:
#                 i += 1
#                 j += 1
#                 k += 1
#                 continue
            
#             if p_len - j >= 2 and p[j] == '.' and p[j+1] == '*':
#                 break
            
#             if p[j] == ".":
#                 i += 1
#                 j += 1
#                 k += 1
#                 continue
            
            
#             if p[j] == '*':
#                 character = s[i]
#                 i += 1
#                 j += 2
#                 k += 1
#                 remaining_length = s_len - i
#                 for _ in range(remaining_length):
#                     print(i)
#                     if s[i] == character:
#                         i += 1
#                         k += 1
#                         continue
#                     break
#                 continue
            
#             i += 1
#             j += 1
#             k += 1
#         return result
                    
        
        
# sol = Solution()
# print(sol.isMatch("aab", 'c*a*b'))