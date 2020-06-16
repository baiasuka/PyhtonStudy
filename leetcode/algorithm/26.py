# 26.删除排序数组中的重复项
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        反向遍历
        :param nums:
        :return:
        """
        if not nums:
            return False
        count = 0
        lenght = len(nums)
        for i in range(-lenght, -1):
            if nums[i + 1] == nums[i]:
                nums.pop(i)
                count += 1
        return lenght - count

