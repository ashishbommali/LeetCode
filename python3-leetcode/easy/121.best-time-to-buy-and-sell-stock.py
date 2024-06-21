#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0      
        right = 1  
        l = len(prices)
        max_profit = 0
        current_profit = 0

        for i in range(1, l):
            print("left", left, "right", right, "current", current_profit)

            if prices[right] < prices[left]:
                left = prices[i]
                right += 1
                current_profit += prices[right] - prices[left]
                        

        return 0

# @lc code=end

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))