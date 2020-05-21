# 9.回文数

class Solution:
    def isPalindromeByStr(self, x: int) -> bool:
        """
        使用字符串转置的方法
        :param x:
        :return:
        """
        if x < 0:
            return False
        x_str = str(x)
        y_str = x_str[::-1]
        if y_str == x_str:
            return True
        else:
            return False

    def isPalindromeByNum(self, x: int) -> bool:
        """
        使用数字运算的方法
        :param x:
        :return:
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        ori_x = x
        temp = 0
        while x != 0:
            temp = temp * 10 + x % 10
            x //= 10
        return temp == ori_x


print(Solution().isPalindrome_by_num(121))