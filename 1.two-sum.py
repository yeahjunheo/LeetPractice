#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Dictionary to store numbers we've seen and their indices
        
        for i, num in enumerate(nums):
            leftOver = target - num
            
            # If the leftover is found in the dictionary, return its index and the current index
            if leftOver in seen:
                return [seen[leftOver], i]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i
            
        return []
        
# @lc code=end

