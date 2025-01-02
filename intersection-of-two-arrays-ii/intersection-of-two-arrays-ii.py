class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        subset_array = []
        if len(nums1) > len(nums2):
            target_nums = nums2
            reference_nums = nums1
        else:
            target_nums = nums1
            reference_nums = nums2
            
        for i in target_nums: 
            if i in reference_nums:
                subset_array.append(i)
                reference_nums.remove(i)
                
        return subset_array
        