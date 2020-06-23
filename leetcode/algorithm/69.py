# 69.x的平方根

class Solution:
    def mySqrt(self, x: int) -> int:
        if x > 1:
            ln = 0
            for i in range(1, x+1):
                di = i*i
                if x == di:
                    return i
                elif x > ln and x < di:
                    return i - 1
                else:
                    ln = di
        else:
            return x

if __name__ == '__main__':
    print(Solution().mySqrt(128))