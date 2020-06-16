# 27.移除元素
class Solution:
    def removeElement(self, nums, val) -> int:
        """

        :param nums: List[int]
        :param val: int
        :return:
        """
        if not nums:
            return False
        count = 0
        lenght = len(nums)
        for i in range(-lenght, 0):
            print(nums[i])
            if nums[i] == val:
                nums.pop(i)
                count += 1
        return lenght - count


if __name__ == '__main__':
    tl = [1,3,2,2,3]
    r = Solution().removeElement(tl, 3)
    print(tl)