class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validateDigits(each_list):
            present = set()
            
            for i in each_list:
                if i != ".":
                    if i in present:
                        return False
                    present.add(i)
            return True
                
        for i in board:
            if not validateDigits(i):
                return False
               
        for i in zip(*board):
            if not validateDigits(i):
                return False
        
        for x in range(0,9,3):
            for y in range(0,9,3):
                sub_box = [
                    board[i][j]
                    for i in range(x,x+3)
                    for j in range(y,y+3)
                    
                ]
                if not validateDigits(sub_box):
                    return False
                
        
        return True
               
