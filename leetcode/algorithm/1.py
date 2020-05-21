# 1.两数之和

class Solution:
    def twoSum(self, nums, target):
        temp_dict = {}
        for pos, value in enumerate(nums):
            if str(target - value) in temp_dict:
                return [pos, temp_dict[str(target - value)]]
            else:
                temp_dict[str(value)] = pos
        return []


r = Solution().twoSum([2, 7, 11, 15], 13)
print(r)