# 53.最大子序和

class Solution:
    def maxSubArray(self, nums) -> int:
        """
        遍历列表，到nums[i]时判断以num[i-1]为结尾的最大子序是否大于0，若小于0则num[i] + 0。
        可理解为当前数字加上负数时必不可能为最大子序和，滑动的子序从当前数重新开始
        :param nums: List[int]
        :return:
        """
        lenght = len(nums)
        if lenght == 1:
            return nums[0]
        sum = nums[0]
        max_sum = nums[0]
        for i in range(1,lenght):
            sum = nums[i] + max(sum, 0)
            max_sum = max(max_sum, sum)
        return max_sum


if __name__ == '__main__':
    r = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(r)
