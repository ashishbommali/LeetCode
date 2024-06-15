#
# @lc app=leetcode id=3146 lang=python3
#
# [3146] Permutation Difference between Two Strings
#

# @lc code=start
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_indexes = {}
        t_indexes = {}
        sum = 0
        
        for i in range(0, len(s)):
            s_indexes[s[i]] = i+1
            t_indexes[t[i]] = i+1

        for key in s_indexes:
            sum += abs(s_indexes[key] - t_indexes.get(key, 0))

        return sum


# @lc code=end
