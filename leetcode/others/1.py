class Solution:
    def longestSubarray(self, nums):
        window_head = 0
        window_tail = 0
        max_len = 0
        flag = 0
        full_one = 1
        full_zero = 1
        for i in nums:
            if i == 1:
                full_zero = 0
                window_head += 1
            else:
                full_one = 0
                if flag == 0:
                    if window_head:
                        flag = 1
                else:
                    if max_len < window_head + window_tail:
                        max_len = window_head + window_tail
                    window_tail = window_head
                    window_head = 0
                    flag = 0
            print(str(i),'--',str(window_tail),'+',str(window_head))
        if full_zero:
            return 0
        if full_one:
            return window_head - 1
        if max_len < window_head + window_tail:
            max_len = window_head + window_tail
        return max_len


tl = [1,0,1,1,1,1,1,1,0,1,1,1,1,1]
print(Solution().longestSubarray(tl))