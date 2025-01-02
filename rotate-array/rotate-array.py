class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        len_nums = len(nums)
        k = k%len_nums
        ### Solution 1
        # if k > 0 :
        #     nums[:] = nums[-k:]+nums[:len_nums-k]
        
        ### Solution 2
        if k > 0 :
            nums.reverse()
            nums[0:k] = reversed(nums[0:k])
            nums[k:] = reversed(nums[k:])
            
        
        
        