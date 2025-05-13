
class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dict_s = {}
        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        
        for _ in range(t):
            new_dict_s = {}
            for c in dict_s:
                if c == 'z':
                    new_dict_s['a'] = new_dict_s.get('a', 0) + dict_s['z']
                    new_dict_s['b'] = new_dict_s.get('b', 0) + dict_s['z']
                else:
                    next_char = chr(ord(c) + 1)
                    new_dict_s[next_char] = dict_s[c]
            dict_s = new_dict_s
            
        return sum(dict_s.values()) % MOD

        
sol = Solution()
print(sol.lengthAfterTransformations("abcyy", 2))