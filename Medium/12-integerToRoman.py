from math import log10
from typing import TypedDict

class SpecialCase (TypedDict):
    roman_value: str
    new_value: int

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        
        def handle_nine_case(value: int) -> SpecialCase:
            result = {
                "roman_value": '0',
                "new_value": 0
            }
            if value >= 900:
                result["roman_value"] = roman_dict[100] + roman_dict[1000]
                result["new_value"] = value % 900
            elif value >= 90:
                result["roman_value"] = roman_dict[10] + roman_dict[100]
                result["new_value"] = value % 90
            elif value >= 9:
                result["roman_value"] = roman_dict[1] + roman_dict[10]
                result["new_value"] = value % 9
            return result
        
        def handle_four_case(value: int) -> dict:
            result = {
                "roman_value": '0',
                "new_value": 0
            }
            if value >= 400:
                result["roman_value"] = roman_dict[100] + roman_dict[500]
                result["new_value"] = value % 400
            elif value >= 40:
                result["roman_value"] = roman_dict[10] + roman_dict[50]
                result["new_value"] = value % 40
            elif value >= 4:
                result["roman_value"] = roman_dict[1] + roman_dict[5]
                result["new_value"] = value % 4
            return result
                
        
        result = ""
        while num > 0:
            first_digit = num // (10 ** int(log10(num)))
            
            if first_digit == 4:
                response = handle_four_case(num) 
                result += response["roman_value"]
                num = response["new_value"]
            
            elif first_digit == 9:
                response = handle_nine_case(num) 
                result += response["roman_value"]
                num = response["new_value"]
            
            elif num >= 1000:
                temp = 0
                while temp + 1000 <= num:
                    temp += 1000
                    result += roman_dict[1000]
                num -= temp
                
            elif num >= 500:
                temp = 0
                while temp + 500 <= num:
                    temp += 500
                    result += roman_dict[500]
                num -= temp
                
            elif num >= 100:
                temp = 0
                while temp + 100 <= num:
                    temp += 100
                    result += roman_dict[100]
                num -= temp
            
            elif num >= 50:
                temp = 0
                while temp + 50 <= num:
                    temp += 50
                    result += roman_dict[50]
                num -= temp
                
            elif num >= 10:
                temp = 0
                while temp + 10 <= num:
                    temp += 10
                    result += roman_dict[10]
                num -= temp
                
            elif num >= 5:
                temp = 0
                while temp + 5 <= num:
                    temp += 5
                    result += roman_dict[5]
                num -= temp
                
            elif num >= 1:
                temp = 0
                while temp + 1 <= num:
                    temp += 1
                    result += roman_dict[1]
                num -= temp
                
                
        return result
        
sol = Solution()
print(sol.intToRoman(3749))