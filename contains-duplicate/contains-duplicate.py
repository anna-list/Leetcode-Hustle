class Solution:
    def containsDuplicate(self, nums: List[int]):
        # using set
        # if len(nums) > len(set(nums)):
        #     return True
        # else:
        #     return False
        
        nums.sort()

        for i in range(0,len(nums) -1 ):
            if nums[i] == nums[i+1]:
                return True
        return False
        
        
            
            