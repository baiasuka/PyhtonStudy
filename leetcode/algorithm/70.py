# 70.爬楼梯

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        类似斐波拉契数列计算，f(n) = f(n-1) + f(n-2)
        :param n:
        :return:
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            r1 = 1
            r2 = 2
            for i in range(3, n+1):
                r2, r1 = (r1 + r2, r2)
            return r2

if __name__ == '__main__':
    print(Solution().climbStairs(18))