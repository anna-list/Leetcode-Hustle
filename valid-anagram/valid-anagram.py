class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        
        for i in range(len(s_list)):
        
            if s_list[i] in t_list:
                t_list.remove(s_list[i])
            else:
                return False
    
        if i == len(s_list)-1 and len(t_list)==0:
            return True
        else:
            return False
                