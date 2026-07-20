class Solution:
    def check_exists(self, ind, prev):
        if ind == len(self.word):
            return True
        
        i, j = prev
        nxt = ind + 1
        
        if i != 0:
            nxt_coor = (i - 1, j)
            
            if nxt_coor not in self.visited and self.board[nxt_coor[0]][nxt_coor[1]] == self.word[ind]:
                self.visited.add(nxt_coor)
                
                if self.check_exists(nxt, nxt_coor):
                    return True
                
                self.visited.remove(nxt_coor)
        
        if j != 0:
            nxt_coor = (i, j - 1)
            
            if nxt_coor not in self.visited and self.board[nxt_coor[0]][nxt_coor[1]] == self.word[ind]:
                self.visited.add(nxt_coor)
                
                if self.check_exists(nxt, nxt_coor):
                    return True
                
                self.visited.remove(nxt_coor)
        
        if i != len(self.board) - 1:
            nxt_coor = (i + 1, j)
            
            if nxt_coor not in self.visited and self.board[nxt_coor[0]][nxt_coor[1]] == self.word[ind]:
                self.visited.add(nxt_coor)
                
                if self.check_exists(nxt, nxt_coor):
                    return True
                
                self.visited.remove(nxt_coor)
        
        if j != len(self.board[0]) - 1:
            nxt_coor = (i, j + 1)
            
            if nxt_coor not in self.visited and self.board[nxt_coor[0]][nxt_coor[1]] == self.word[ind]:
                self.visited.add(nxt_coor)
                
                if self.check_exists(nxt, nxt_coor):
                    return True
                
                self.visited.remove(nxt_coor)
        
        return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.visited = {(i, j)}
                    
                    if self.check_exists(1, (i, j)):
                        return True
                    
        return False