class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_indices = []
        for i in range(0,len(nums)):
            delta_value = target - nums[i]
            for j in (range(i+1,len(nums))):
                if delta_value == nums[j]:
                    target_indices.append(i)
                    target_indices.append(j)
                    break
            
        return target_indices