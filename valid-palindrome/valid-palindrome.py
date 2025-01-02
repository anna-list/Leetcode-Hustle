class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for i in s:
            if i.isalnum():
                clean_s = clean_s + i.lower()
        len_s = len(clean_s) - 1
        matched = 0
        check_point = floor(len(clean_s)/2)
        list_s = list(clean_s)
        
        for iter_val in range(0,check_point):
            if list_s[iter_val] == list_s[len_s-iter_val]:
                matched = matched + 1
            else:
                return False
        if matched == check_point:
            return True
        