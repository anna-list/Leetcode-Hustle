class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        lcp = strs[0]
        for i in strs[1:]:
            while not i.startswith(lcp):
                lcp = lcp[:-1]
                if len(lcp) == 0:
                    return ""
            
        return lcp
            
        
        
            
        
        
        
        
            
            
        