#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        unique = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if unique == nums[i]:
                continue
            else:
                
                index += 1
                unique = nums[i]
                nums[index] = nums[i]
                count +=1 
                
        return count
# @lc code=end