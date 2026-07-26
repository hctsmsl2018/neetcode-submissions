class Solution:
    def get_decodings(self, ind):
        if ind == len(self.s):
            return 1
        
        if self.memo[ind] == -1:
            tot = 0
            
            if self.s[ind] == '0':
                return 0
            else:
                tot += self.get_decodings(ind + 1)
            
            if ind <= len(self.s) - 2 and int(self.s[ind: ind + 2]) <= 26:
                tot += self.get_decodings(ind + 2)
                
            self.memo[ind] = tot
                
            return tot
        else:
            return self.memo[ind]
    
    def numDecodings(self, s: str) -> int:
        self.s = s
        self.memo = [-1] * len(s)
        
        return self.get_decodings(0)