#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nams = nums.sort()
        
        for i in range(len(nums)):
            leftOver = target - nams[i]
            
            if leftOver in nums:
                return [i, nums.index(leftOver)]
            
        return False
            
        
# @lc code=end

