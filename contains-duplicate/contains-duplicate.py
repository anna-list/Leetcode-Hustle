class Solution:
    def containsDuplicate(self, nums: List[int]):
        if len(nums) > len(set(nums)):
            return True
        else:
            return False
        