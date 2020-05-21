# 13.罗马数字转整数

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        普通循环解法
        :param s:
        :return:
        """
        letters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for pos in range(len(s)):
            if pos < len(s)-1 and letters[s[pos]] < letters[s[pos+1]]:
                result -= letters[s[pos]]
            else:
                result += letters[s[pos]]
        return result

    def romanToIntByRE(self, s: str) -> int:
        """
        使用正则表达式的解法
        :param s:
        :return:
        """
        import re
        letters = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sp_letters = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        result = 0
        sp_words = re.findall("IV|IX|XL|XC|CD|CM", s)
        for i in sp_words:
            result += sp_letters[i]
        others = re.sub("IV|IX|XL|XC|CD|CM", "", s)
        for j in others:
            result += letters[j]
        return result




