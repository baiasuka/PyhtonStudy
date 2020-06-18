# 38.外观数列

class Solution:
    def countAndSay(self, n: int) -> str:
        """
        遍历字符串对连续字符计数后以（连续长度）+（连续字符）分段拼接
        :param n:
        :return:
        """
        if n == 1:
            return '1'
        else:
            last_str = '1'
            for i in range(2, n + 1):
                head = last_str[0]
                counter = 0
                new_str = ''
                for word in last_str:
                    if word == head:
                        counter += 1
                    else:
                        if counter > 0:
                            new_str += str(counter) + head
                            counter = 1
                            head = word
                new_str += str(counter) + head
                last_str = new_str
            return last_str

if __name__ == '__main__':
    r = Solution().countAndSay(6)
    print(r)


