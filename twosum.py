from sre_compile import JUMP
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            secondNum = target - nums[i]
            try:
                j = nums.index(secondNum)
                if j != i:
                    return [i, j]
            except:
                continue
