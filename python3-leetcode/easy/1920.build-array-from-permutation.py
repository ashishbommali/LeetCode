#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#
from typing import List

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(nums[i])

        return l
# @lc code=end

