#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if index != i:
                    nums[index] = nums[i]
                index += 1
        
        return index
# @lc code=end

# s = Solution()
# print(s.removeElement([3,2,2,3],3))
# print(s.removeElement([0,1,2,2,3,0,4,2], 2))