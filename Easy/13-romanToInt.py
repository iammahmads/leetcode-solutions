class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
       
        n = result = 0
        s_len = len(s)
        while n < s_len:
            if s[n] == "M":
                result += roman_dict["M"]
                n += 1
            
            elif s[n] == "D":
                result += roman_dict["D"]
                n += 1
               
            elif s[n] == "C":
                if n + 1 < s_len and s[n+1] == "D":
                   result += roman_dict["D"] - roman_dict["C"]
                   n += 2
                   continue
                if n + 1 < s_len and s[n+1] == "M":
                   result += roman_dict["M"] - roman_dict["C"]
                   n += 2
                   continue
                result += roman_dict["C"]
                n += 1
            
            elif s[n] == "L":
                result += roman_dict["L"]
                n += 1
                
            elif s[n] == "X":
                if n + 1 < s_len and s[n+1] == "L":
                   result += roman_dict["L"] - roman_dict["X"]
                   n += 2
                   continue
                if n + 1 < s_len and s[n+1] == "C":
                   result += roman_dict["C"] - roman_dict["X"]
                   n += 2
                   continue
                result += roman_dict["X"]
                n += 1
                
            elif s[n] == "V":
                result += roman_dict["V"]
                n += 1
                
            elif s[n] == "I":
                if n + 1 < s_len and s[n+1] == "V":
                   result += roman_dict["V"] - roman_dict["I"]
                   n += 2
                   continue
                if n + 1 < s_len and s[n+1] == "X":
                   result += roman_dict["X"] - roman_dict["I"]
                   n += 2
                   continue
                result += roman_dict["I"]
                n += 1
                
        return int(result)
    
sol = Solution()
print(sol.romanToInt("MCMXCIV"))