#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        min_length = float('inf')
        sum = beg = end = 0
        for i in nums:
            sum += i
            
            print("beg", beg,"end",end,"sum",sum)
            if sum > target:
                print("sum > target: before deduction", sum)
                sum -= nums[beg]
                beg += 1
                print("sum > target: after deduction", sum, "beg", beg)
            
            if sum < target:
                end += 1

            print("beg", beg,"end",end)

            if sum == target:
                min_length = min(min_length, end-beg+1)
                print("min_length", min_length)

        if sum == target:
            return min_length    
        
        if sum != target:
            return 0

# @lc code=end

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
# print(s.minSubArrayLen(4, [1,4,4]))
# print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))