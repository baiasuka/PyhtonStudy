# 67.二进制求和

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ml = max(len(a), len(b))
        a = a.rjust(ml, '0')
        b = b.rjust(ml, '0')
        ad = 0
        r = ''
        for i in range(1, ml + 1):
            if (int(a[ml - i]) + int(b[ml - i]) + ad) == 3:
                r = '1' + r
                ad = 1
            elif (int(a[ml - i]) + int(b[ml - i]) + ad) == 2:
                r = '0' + r
                ad = 1
            elif (int(a[ml - i]) + int(b[ml - i]) + ad) == 1:
                r = '1' + r
                ad = 0
            else:
                r = '0' + r
                ad = 0
        if ad == 1:
            r = '1' + r
        return r

if __name__ == '__main__':
    print(Solution().addBinary('11', '1'))
