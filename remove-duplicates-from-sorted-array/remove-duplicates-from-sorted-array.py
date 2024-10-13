class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        # start the pointer from the first element of the list
        i = 0
        
        #start the other pointer from the second element until the end of the list
        print(len(nums))
        for j in range(1,len(nums)):
            print(j)
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        
        print(i)
        print(nums)
        return i+1
        
        