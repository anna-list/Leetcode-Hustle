class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        factor = len(digits)-1
        numerical_value = 0
        for i in range(0,len(digits)):
            numerical_value += (10**factor) * digits[i]
            factor -= 1 
            
        numerical_value = numerical_value + 1
        list_output = [int(each_digit) for each_digit in str(numerical_value)]
        return list_output
    
    