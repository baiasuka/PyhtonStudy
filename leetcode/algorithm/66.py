# 66.加一

class Solution:
    def plusOne(self, digits):
        """
        本例使用递归解法，进位则对前面的数字做加一操作
        :param digits: List[int]
        :return: List[int]
        """
        if digits == [9]:
            return [1, 0]
        if digits[-1] + 1 == 10:
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
            return digits

if __name__ == '__main__':
    print(Solution().plusOne([9,9,9]))
