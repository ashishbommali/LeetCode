#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#
from typing import List
# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return (nums+nums)
        
# @lc code=end

sol = Solution()
print(sol.getConcatenation([1,2,3]))