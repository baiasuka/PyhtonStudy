# 给定一个长度为 n 的数组，请你编写一个函数，返回该数组排序后的结果。
#
# 数据范围： 0 ≤n≤1000000，数组中每个元素都满足 0 ≤val≤1000000000
# 要求：空间复杂度 O(n)，时间复杂度 O(nlogn)
from typing import List


class Solution:
    def MySort(self , arr: List[int]) -> List[int]:
        # write code here