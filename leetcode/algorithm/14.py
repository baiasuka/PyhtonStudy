# 14.最长公共前缀

class Solution:
    def longestCommonPrefix(self, strs):
        if strs:
            from functools import reduce
            shortest = reduce(lambda x, y: x if len(x) < len(y) else y, strs)
            min_len = len(shortest)
            common_head = ""
            for i in range(min_len):
                letter = shortest[i]
                for words in strs:
                    if words[i] != letter:
                        return common_head
                common_head += letter
            return common_head
        else:
            return ""

print(Solution().longestCommonPrefix([]))