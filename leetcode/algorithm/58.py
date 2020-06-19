# 58.最后一个单词长度

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        字符串切片取最后存在的单词（分隔出的空字符串不计入），求其长度即可
        :param s:
        :return:
        """
        tl = [i for i in s.split(' ') if i]
        return len(tl[-1]) if tl else 0



if __name__ == '__main__':
    r = Solution().lengthOfLastWord(' ')
    print(r)