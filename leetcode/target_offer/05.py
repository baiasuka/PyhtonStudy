# 剑指 Offer 05. 替换空格
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
# 示例 1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

class Solution:
    def replaceSpace(self, s: str) -> str:
        r = s.replace(' ', '%20')
        return r


