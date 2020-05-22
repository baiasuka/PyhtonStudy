# 20.有效括号
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        temp_stack = []
        brackets_tail = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        brackets_head = brackets_tail.values()
        head_count = 0
        tail_count = 0
        for ind, val in enumerate(s):
            if val in brackets_tail:
                tail_count += 1
                if len(temp_stack) > 0:
                    r = temp_stack.pop(-1)
                else:
                    return False
                if r != brackets_tail[val]:
                    return False
            elif val in brackets_head:
                head_count += 1
                temp_stack.append(val)
            else:
                return False
        if head_count != tail_count:
            return False
        return True

print(Solution().isValid("){"))
