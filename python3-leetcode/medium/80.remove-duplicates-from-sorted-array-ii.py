#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      
        index = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count += 1
            else: 
                count = 1

            if count <= 2:
                nums[index] = nums[i]
                index += 1
            else:
               continue

        return index
        
# @lc code=end
