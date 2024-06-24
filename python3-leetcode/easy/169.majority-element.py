from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = Counter(nums)
        # print(Counter(nums).most_common(1))
        value = max(x.values())
        
        if value > len(nums)/2:
        
            return list(x.keys())[list(x.values()).index(value)]

s = Solution().majorityElement([2,2,2,2,2,1,1,2,2])
print(s)