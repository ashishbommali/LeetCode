#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#
from typing import List
# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # not_grumpy = 0
        
        # for i in range(0, len(customers)):
        #     if grumpy[i]==0:
        #         not_grumpy += customers[i]
        
        # print(not_grumpy)

        # strategy_value = 0
        # maximised_output = 0
        
        # for i in range(minutes):
        #     if grumpy[i] == 1:
        #         maximised_output += customers[i]
        
        # strategy_value += maximised_output
        # print(i,strategy_value)

        # max_profit = 0
        
        # for i in range(minutes, len(customers)-minutes+1):
        #     sum = 0
        #     for j in range(i, i+minutes):
        #         if grumpy[j] == 1:
        #             sum += customers[j]
        #             if max_profit <= sum:
        #                 max_profit = sum
            
        #     print("sliding stat max: ",i,j,customers[i:j], max_profit)
          

        # return (not_grumpy + strategy_value + max_profit)

        not_grumpy = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        
        current_additional = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)
        max_additional = current_additional
        
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                current_additional += customers[i]
            if grumpy[i - minutes] == 1:
                current_additional -= customers[i - minutes]
            max_additional = max(max_additional, current_additional)
        
        return not_grumpy + max_additional
# @lc code=end

s = Solution()
#print(s.maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
# print(s.maxSatisfied([3,2,5],[0,1,1],2))
# print(s.maxSatisfied([1],[1],1))
# print(s.maxSatisfied([1,2],[0,1],1))