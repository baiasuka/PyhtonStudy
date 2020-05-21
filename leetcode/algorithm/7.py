# 7.整数反转

class Solution:
    def reverse(self, x: int) -> int:
        tn = str(x)
        if tn[0] == "-":
            rn = "-" + (tn[1:])[::-1].lstrip('0')
            if int((tn[1:])[::-1].lstrip('0')) > 2 ** 31:
                return 0
            else:
                return int(rn)
        else:
            rn = (tn)[::-1].lstrip('0')
            if rn == '' or int(rn) > 2 ** 31 - 1:
                return 0
            else:
                return int(rn)


r = Solution().reverse(123)
print(r)