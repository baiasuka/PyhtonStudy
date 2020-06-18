# 35.搜索插入位置

class Solution:
    """
    考察的是查找，可说的是各类查找方法（顺序、二分、树）
    """
    def searchInsertByBinary(self, nums, target) -> int:
        """
        因为是有序表，可使用二分法查找
        :param nums: List[int]
        :param target: int
        :return:
        """
        if nums:
            if target <= nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            ln = 0
            rn = len(nums) - 1
            mid = rn // 2
            while ln < mid:
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    ln = mid
                    mid = (rn + ln) // 2
                else:
                    rn = mid
                    mid = (rn + ln) // 2
            return mid + 1
        else:
            return False

