# 1.两数之和

class Solution:
    """
    实际考察的是哈希表，将值作为字典的key，值的位置作为字典的value
    """
    def twoSum(self, nums, target):
        temp_dict = {}
        for pos, value in enumerate(nums):
            if str(target - value) in temp_dict:
                return [pos, temp_dict[str(target - value)]]
            else:
                temp_dict[str(value)] = pos
        return []

if __name__ == '__main__':
    r = Solution().twoSum([2, 7, 11, 15], 13)
    print(r)